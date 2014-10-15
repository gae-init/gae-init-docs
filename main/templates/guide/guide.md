So after wetting your appetite in the [Tutorial]({{url_for('tutorial')}}) we
will now give you the big picture overview of the gae-init environment. After
reading this guide you should understand how the individual blocks of gae-init
play together, how you can benefit most of them and where to start in case you
want to customise things.

{% raw %}

Overview {#overview}
--------

- [Interplay of components](#interplay)
    - [run.py](#run_py)
    - [config.py](#config_py)
    - [appcfg & app.yaml](#appengine)
    - [server side tasks](#server_side_tasks) (setup, compiling, minification, bundling)
        - [Node.js / npm](#node)
        - [Grunt](#grunt)
        - [Bower](#bower)
        - [livereload](#livereload)
        - [CoffeeScript](#coffeescript)
        - [UglifyJS / JS Minification](#uglifyjs)
        - [Less & CSS Minification](#less)
    - [server side libs](#server_side_libs) (Python)
    - [client side libs](#client_side_libs) (JS)
- [main.py](#main_py)
- [templates/base.html](#templates_base)
    - [available blocks](#templates_blocks)
    - [bits](#templates_bits) (especially style + js)
- [Frequent tasks / dev workflows](#workflows)
    - [running the dev-server](#run_dev_server)
    - [customize styles](#custom_styles)
    - [custom JavaScript / CoffeeScript](#custom_js)
    - [add a new Python lib](#new_python_lib)
    - [add a new / update/reinstall JS lib(s)](#new_js_lib) (Bower)
    - [add a new page](#new_page)


Interplay of components {#interplay}
--------------------------------------
gae-init is built on top of several tools that try to ease your job as developer
by supporting common tasks. In order to be awesome you have to know these little
helpers and how they work together, so let's get you on the line.

### run.py {#run_py}
It all starts with `./run.py` which you might still know from the
[Tutorial]({% endraw %}{{url_for('tutorial')}}{% raw %}). As its name implies it
runs your dev-server on [http://localhost:8080](http://localhost:8080) with
`./run.py -s`. This is done by invoking AppEngine's `dev_appserver.py`
internally. While `./run.py` will wrap certain common arguments to that, it's
possible to pass additional arg along with the `--appserver-args` option. So
if you for example want to see debug logging output of your app in the terminal,
you can run: `./run.py -s --appserver-args --log_level debug`.

What we didn't mention in the Tutorial is that you typically want to start a
second `./run.py -w` in a different terminal window to watch for changes in
`*.coffee` and `*.less` files and automagically trigger a recompilation (also
see our Frequent Tasks section [running the dev-server](#run_dev_server) for
some more included batteries).

`./run.py` can also flush your dev-server's datastore `-f`, so you can start
from scratch with a fresh store without worrying about interference with already
existing objects in it from previous runs.

`./run.py -m` will minify and bundle together your `*.js` and `*.css` files
(manually generated ones, the ones from installed libs as well as the ones
generated from CoffeeScript and Less). On your dev-server you will normally not
see the minified version of your page as it is cumbersome for debugging, but in
production the minification can drastically reduce the size and amounts of
requests to your page (in case of this docs page from 49 to 28) and thereby
increase your page load speed. Therefore, you need to run `./run.py -m` before
deploying your app. If you want to see the effects without deploying feel free
to temporarily set `PRODUCTION=True` in your `config.py`. Be aware of the fact
that the minified files don't auto-update though, so you need to re-run the
minification if you change something in your scripts or styles.

Last but not least `./run.py -C` will clean up and reinstall all the local
tools and libraries that were downloaded via Node and Bower to their latest
versions. This should be used whenever you want to update your 3rd party
libraries and tools. See also the [Node.js](#node), [Bower](#bower) and
[add a new / update/reinstall js lib(s)](#new_js_lib) sections below.

For completeness also have a look at our
[Run Script]({% endraw %}{{url_for('run')}}{% raw %}) page or have a look into
[run.py](https://github.com/gae-init/gae-init/blob/master/run.py)'s code.


### config.py {#config_py}
[config.py](https://github.com/gae-init/gae-init/blob/master/main/config.py)
is a central place to orchestrate the gae-init toolbox.

`run.py` for example needs to know a couple of things for its various tasks
like minification and compiling: which are the relevant Less, JavaScript and
CoffeeScript files. `run.py` takes these from `config.py` which defines
`SCRIPTS` and `STYLES`. The same `SCRIPTS` are used by some magic in
[/main/templates/bit/script.html](https://github.com/gae-init/gae-init/blob/master/main/templates/bit/script.html)
to load the minified and bundled JavaScript in production as well as the actual
source files on the dev-server.
This means that if you want to make use of the minification feature, be sure
to add your javascript files to the `SCRIPTS` section in `config.py`. This has
the added benefit that you don't need to manually link them in your HTML, but
that the script bit can do its magic. (See the
[API reference on config.py]({% endraw %}{{url_for('reference')}}{% raw %}#config.STYLES)
as well as [add a new js lib](#new_js_lib) and [template bits](#templates_bits)
below for further information.)

Apart from that `config.py` also sets some other important global constants
like `PRODUCTION` which is `true` if deployed and run on the actual Google App
Engine infrastructure and `DEVELOPMENT` and `DEBUG` which are `true` when run
on the dev-server. `config.py` also extracts version information and the
application id into `CURRENT_VERSION_ID`, `CURRENT_VERSION_NAME`,
`CURRENT_VERSION_TIMESTAMP`, `CURRENT_VERSION_DATE` and `APPLICATION_ID` (see
[API reference on config.py]({% endraw %}{{url_for('reference')}}{% raw %}#config)
for more).

`CONFIG_DB` and `SECRET_KEY` encapsulate the datastore's singleton config
object as well as the secret key which is randomly autogenerated on first run
of your app and used in Flask for cookie protection (session cookies and auth).

`DEFAULT_DB_LIMIT` is used for the default paging size in lists (see
[utils.retrieve_dbs](https://github.com/gae-init/gae-init/blob/master/main/util.py#L52)
for more on this).


### appcfg & app.yaml {#appengine}
As every other App Engine app you will find the main configurations (e.g., the
app's name, its programming language, the main handler definitions, ...) in
[main/app.yaml](https://github.com/gae-init/gae-init/blob/master/main/app.yaml).

The main handler definitions include serving the `main/static` dir under `/p/`
and invoke `main/main.app` (so the app object defined in
[main/main.py](https://github.com/gae-init/gae-init/blob/master/main/main.py)
for nearly everything else.

`app.yaml` also defines `skip_files`, so what not to upload. Notice how
`lib/.*`, `static/dst/.*`, some folders from `static/ext/` and `static/src/.*`
are excluded. The reason for these to be excluded is the minification process
as described for `./run.py -m` above and configured in `config.py`. This means
that before deployment you need ot run `./run.py -m` as your production server
will otherwise lack critical libraries at runtime. This also means that you
should not place own libraries or files in these folders manually without
adding them to `config.py`.

After running `./run.py -m` you can deploy the app with Google App Engine's
tools as usual, either from command line with `appcfg.py` or via the
GoogleAppEngineLauncher app.



### server side tasks (setup, compiling, minification, bundling) {#server_side_tasks}
As you know by now gae-init takes care to setup, compile, minify and bundle
many files before you can deploy them. For this it makes use of well established
tools for web development.

On invocation of `./run.py -s` gae-init will first check that some basic tools
it needs are installed. If not it will print a message pointing you to our
[requirements]({% endraw %}{{url_for('requirement')}}{% raw %}) page which
explains how to install them. If those basic requirements are installed they'll
be used to pull in the remaining tech-stack and setup everything else in the
app's directory (it's magic).

Most of this magic actually happens in
[run.py](https://github.com/gae-init/gae-init/blob/master/run.py#L381)'s
`install_dependencies()` function. It first creates the `/temp` dir in your
app's folder if it isn't there. It then runs through the following steps about
which you can read more in the following sections:

 - [`npm install`](#node)
 - [`grunt ext`](#grunt)
     - this will run [`bower install`](#bower)
 - [`(venv) pip install`](#server_side_libs)

In general each of these steps is only executed if it has either never been
run or if the corresponding config files have been changed since the last run.
If you think something went wrong you can always start fresh by running
`./run -C`.


#### Node.js / npm {#node}
[Node.js](http://nodejs.org) is a JavaScript runtime environment which allows
us to run js code from the command line. We first use it for its package
manager npm to first run `npm install`
([docs](https://www.npmjs.org/doc/cli/npm-install.html)) which installs all the
the `dependencies` and `devDependencies` from
[/package.json](https://github.com/gae-init/gae-init/blob/master/package.json).

These dependencies end up in the `/node_modules` folder and are server side js
libraries (so to be super explicit: they're never directly used by clients
(browsers) of your app in the end, they rather help you during development and
are run by you either directly or through `./run.py`).

A couple of things that are installed by this (at the time of writing this) are

 - [CoffeeScript](#coffeescript)
 - [Less](#less)
 - [UglifyJS](#uglifyjs)
 - [Bower](#bower)
 - [Grunt](#grunt) (and several extensions)


#### Grunt {#grunt}
[Grunt](http://gruntjs.com) is a "JavaScript task runner". We mainly use it to
wipe certain directories, run [Bower](#bower) from it and watch certain files
for changes.

For this we use several Grunt extensions:

   - [load-grunt-tasks](https://github.com/sindresorhus/load-grunt-tasks)
     Load multiple grunt tasks using globbing patterns.
   - [grunt-bower-task](https://github.com/yatskevich/grunt-bower-task)
     Bower integration.
   - [grunt-contrib-clean](https://github.com/gruntjs/grunt-contrib-clean)
     Clear files and folders.
   - [grunt-contrib-watch](https://github.com/gruntjs/grunt-contrib-watch)
     Run tasks whenever watched files change.

Grunt is configured in
[/Gruntfile.coffee](https://github.com/gae-init/gae-init/blob/master/Gruntfile.coffee).
As can be seen, `load-grunt-tasks` is used to auto-load all `"grunt-*"`
extensions defined in `/package.json`. `grunt-contrib-watch` is set up to watch
over changes to `'main/static/**/*.css'` and `'main/**/*.{py,js,html}'` triggers
a [livereload](#livereload) if any of those change. `grunt-contrib-clean` is set
up to clean files in `main/static/{ext,min,dst}`.

Last but not least `grunt-bower-task` is configured to correctly invoke bower
as explained [below](#bower), and `grunt ext` is defined to clean the
`main/static/ext` folder and then run Bower. As mentioned
[above](#server_side_tasks) `grunt ext` is invoked in `run.py`'s
`install_dependencies()`.


#### Bower {#bower}
[Bower](http://bower.io/) is "a package manager for the web". We use it to
download and install the packages (e.g., js libraries) that in the end reach
your clients (browsers). Examples for such packages are
[jQuery](http://jquery.com/) and [Bootstrap](http://getbootstrap.com/).
As Bower is invoked through `grunt` with
[grunt-bower-task](https://github.com/yatskevich/grunt-bower-task) a part of its
config is found in
[/Gruntfile.coffee](https://github.com/gae-init/gae-init/blob/master/Gruntfile.coffee).
There you can see that bower installs packages under `main/static/ext` and that
we use`type/component` layout by default (e.g., `js/bootstrap/tooltip.js`,
`js/jquery/jquery.js`, `less/bootstrap/tooltip.less`).

With this initial config, Bower then reads
[/bower.json](https://github.com/gae-init/gae-init/blob/master/bower.json) and
installs its dependencies. At the time of this writing, the installed packages
are `bootstrap`, `font-awesome`, `jquery`, `moment` and `nprogress`.
For each of the dependencies make sure to define a section in `exportsOverride`
that collects all files of the respective types (e.g., have a look at the
`bootstrap` section in that file).


#### livereload {#livereload}
As mentioned [before](#grunt), the default `grunt` task is a `grunt watch` task
which makes the browser reload the page from dev-server if any of the files
change. This is done by a special `livereload.js` which is served by
`grunt watch` and loaded via
[/main/templates/bit/script.html](https://github.com/gae-init/gae-init/blob/master/main/templates/bit/script.html)
on the dev-server.


#### CoffeeScript {#coffeescript}
[CoffeeScript](http://coffeescript.org/) "is a little language that compiles
into JavaScript" and "is an attempt to expose the good parts of JavaScript in a
simple way". In gae-init we use it to compile `*.coffee` files defined in
`SCRIPTS` in
[config.py](https://github.com/gae-init/gae-init/blob/master/main/config.py)
into JavaScript files. This is invoked from `./run.py` by one of the `-s`, `-c`,
`-w` flags via the `compile_all_dst()` function. The corresponding result JS
files will be placed inside the `main/static/dst/script` folder (listed non
`.coffee` files from the `main/static/src/script` folder are just copied). From
there they are picked up directly on the dev-server (via some magic in
[/main/templates/bit/script.html](https://github.com/gae-init/gae-init/blob/master/main/templates/bit/script.html)).
For production the [minification process](#uglifyjs) picks them up.


#### UglifyJS / JS Minification {#uglifyjs}
In gae-init we use [UglifyJS](https://github.com/mishoo/UglifyJS) to compress
the JS files listed in the blocks in `SCRIPTS` in `config.py` into a single
minified JS file in `/main/static/min/script/` per block. This is done with the
`./run.py -m` invocation. For each block the
[CoffeeScript files are compiled](#coffeescript), the resulting or original JS
files concatenated into a single file and then minified by UglifyJS into a
`.min.js` file.


#### Less & CSS Minification {#less}
[Less](http://lesscss.org/) "is a CSS pre-processor". It is widely used, for
example by [Bootstrap](http://getbootstrap.com/). In gae-init we use it to
compile `*.less` files listed in `STYLES` in
[config.py](https://github.com/gae-init/gae-init/blob/master/main/config.py)
into CSS files. This happens similarly to the
[aforementioned CoffeeScript compilation](#coffeescript) by several of the
`./run.py` flags. As Less also directly supports inclusion, currently
`config.py` only includes a single reference to
[/main/static/src/style/style.less](https://github.com/gae-init/gae-init/blob/master/main/static/src/style/style.less).
Inside this the other relevant stylesheets are then included. This has the nice
side-effect of them being in a single big resulting `style.css` file already,
which is put in the `main/static/dst/style` folder. From there it's picked up
by the dev-server. For production `./run.py -m` invokes Less with the `-x` style
to create a minified version of each of the `STYLES` in `config.py` in the
`main/static/min/style` folder. The magic in
[/main/templates/bit/style.html](https://github.com/gae-init/gae-init/blob/master/main/templates/bit/style.html)
makes sure to load the right `style.css` / `style.min.css` in dev-server /
production.



### server side libs (Python) {#server_side_libs}
Python libraries are in general installed with pip via the
[requirements.txt](https://github.com/gae-init/gae-init/blob/master/requirements.txt)
file in the basedir. You can specify necessary libraries in it. The next run of
`./run.py -s` will install new libaries into a virtual environment in the
`temp/venv` folder and then copy them into `main/lib`.

[appengine_config.py](https://github.com/gae-init/gae-init/blob/master/main/appengine_config.py)
will take care that the `sys.path` is modified at runtime to include these libs
so they can simply be imported. On the dev-server the lib folder is added to
the path as is (`sys.path.insert(0, 'lib')`), but in production the lib folder
is zipped by `run.py -m` ([see above](#run_py)) and so all libraries are
imported from one single file called `lib.zip`.

In case you need to include libraries which do not work when zipped you can
create a `main/libx` folder and manually copy those libraries to it. The folder
is included in the `sys.path` on both, the development server and in
production. Don't manually copy libraries into the `main/lib` folder as it is
excluded in [app.yaml](#appengine) and won't be uploaded to App Engine (as its
contents are uploaded in a zipped form as described above).



### client side libs (js) {#client_side_libs}
Client side libs / packages can easily be installed via [Bower](#bower).



main.py {#main_py}
--------------------


templates/base.html {#templates_base}
---------------------------------------

### available blocks {#templates_blocks}

### bits (especially style + js) {#templates_bits}



Frequent tasks / dev workflows {#workflows}
---------------------------------------------

### running the dev-server {#run_dev_server}
You can simply run the server from the project directory (one above main) by
executing `run.py` in a terminal with the `-s` flag.
```bash
$ cd /path/to/project-name
$ ./run.py -s
```
Not only will this start the server
[http://localhost:8080/](http://localhost:8080/), but it will also
make sure that all dependencies are checked and install them if necessary.
Furthermore, it will trigger an initial compilation of the CoffeeScript and Less
files to JavaScript and CSS files so your browser has some JavaScript and
stylesheets when visiting the dev webserver.

While this should get your basic server up and running, in order not to have to
restart it manually whenever you for example change some CoffeeScript
(`*.coffee`) or Less (`*.less`) files, we suggest to run two more commands at
the same time in separate terminals:
```bash
$ ./run.py -w
```
This will watch CoffeeScript and Less files and trigger a recompilation whenever
they are changed.

And:
```bash
$ ./node_modules/.bin/grunt
```
This will provide a watch-daemon, which thanks to `livereload.js`, which is
embedded in the development mode, will automatically reload the pages in your
browser window when any of the relevant files change. Cool, eh? ;)

If the path to grunt seems a bit weird: you can also safely install it globally:
```bash
$ npm install -g grunt-cli
```
After this you can just run grunt from the project root:
```bash
$ grunt
```


### customize styles {#custom_styles}
In order to customize the style of your page you can edit or in most cases
simply add further files in
[main/static/src/style](https://github.com/gae-init/gae-init/blob/master/main/static/src/style),
the main file being
[style.less](https://github.com/gae-init/gae-init/blob/master/main/static/src/style/style.less).
If you add further files make sure to include them in `style.less`.

[Less](#less) is a powerful CSS generation language that will help
you to not repeat yourself while writing your stylesheets. In the case of
`style.less` you will mainly find it including other files. Have a look at them
and at our section about [templates/base.html](#templates_base) in order to
understand what's going on.



### custom JavaScript / CoffeeScript {#custom_js}

### add a new Python lib {#new_python_lib}

### add a new / update/reinstall js lib(s) (bower) {#new_js_lib}

### add a new page {#new_page}

{% endraw %}
