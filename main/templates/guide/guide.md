{% raw %}
So after wetting your appetite in the [Tutorial]({{url_for('tutorial')}}) we
will now give you the big picture overview of the gae-init environment. After
reading this guide you should understand how the individual blocks of gae-init
play together, how you can benefit most of them and where to start in case you
want to customise things.


Overview { #overview }
--------

- [interplay of components](#interplay)
    - [run.py](#run_py)
    - [config.py](#config_py)
    - [appcfg & app.yaml](#appengine)
    - [server side tasks](#server_side_tasks) (setup, compiling, minification, bundling)
        - [Node.js](#node)
        - [Grunt](#grunt)
        - [Bower](#bower)
        - [livereload](#livereload)
        - [CoffeeScript](#coffeescript)
        - [Less](#less)
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


To be done:
===========


interplay of components { #interplay }
--------------------------------------
### run.py { #run_py }

### config.py { #config_py }

### appcfg & app.yaml { #appengine }

### server side tasks (setup, compiling, minification, bundling) { #server_side_tasks }

#### Node.js { #node }

#### Grunt { #grunt }

#### Bower { #bower }

#### livereload { #livereload }

#### CoffeeScript { #coffeescript }

#### Less { #less }

### server side libs (Python) { #server_side_libs }

### client side libs (js) { #client_side_libs }



main.py { #main_py }
--------------------


templates/base.html { #templates_base }
---------------------------------------

### available blocks { #templates_blocks }

### bits (especially style + js) { #templates_bits }



Frequent tasks / dev workflows { #workflows }
---------------------------------------------

### running the dev-server { #run_dev_server }
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
(`*.coffee`) or Less (`*.less`) files, we suggest that run two more commands at
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
This will provide a watch-daemon which thanks to a the `livereload.js` which is
embedded in the development mode will automatically reload the pages in your
browser window when any of the relevant files change. Cool, eh? ;)

If the path to grunt seems a bit weird: you can also safely install it globally:
```bash
$ npm install -g grunt-cli
```
After this you can just run grunt from the project root:
```bash
$ grunt
```


### customize styles { #custom_styles }

### custom JavaScript / CoffeeScript { #custom_js }

### add a new Python lib { #new_python_lib }

### add a new / update/reinstall js lib(s) (bower) { #new_js_lib }

### add a new page { #new_page }

{% endraw %}
