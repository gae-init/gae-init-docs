The easiest way to add a frontend library is to add it as a dependecy in the
[`bower.json`](https://github.com/gae-init/gae-init/blob/master/bower.json),
update some possible overrides and finally execute the `gulp` command if it's
not already running. Once installed you can simply include the styles in the
[`styles.less`](https://github.com/gae-init/gae-init/blob/master/main/static/src/style/style.less)
and the scripts by updating the `ext` section in
[`config.coffee`](https://github.com/gae-init/gae-init/blob/master/gulp/config.coffee).

By following these steps you will not need to add the third party libraries
into your repository and everything will be minified before deployment.

If you are not able to include it as a bower dependency, simply create a new
folder under the
[`main/static/`](https://github.com/gae-init/gae-init/tree/master/main/static)
directory and include them as descibed in the steps above.

> Check out an example on how to include
[Bootswatch](https://github.com/gae-init/gae-init/pull/360/files),
[Underscore](https://github.com/gae-init/gae-init/pull/438/files) or
[NProgress](https://github.com/gae-init/gae-init/pull/437/files).
