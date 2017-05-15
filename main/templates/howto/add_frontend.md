The easiest way to add a frontend library is:

1. Add it as a dependency in the
   [`bower.json`](https://github.com/gae-init/gae-init/blob/master/bower.json), or try from console `bower install --save dependency-name`
2. Update the overrides in [`bower.json`](https://github.com/gae-init/gae-init/blob/master/bower.json), if necessary.
3. Include the the styles in the
   [`styles.less`](https://github.com/gae-init/gae-init/blob/master/main/static/src/style/style.less).
4. Include the scripts by updating the `ext` section in
   [`config.coffee`](https://github.com/gae-init/gae-init/blob/master/gulp/config.coffee). Note that if your front-end library has dependencies on other libraries being loaded, you will need to add them in here, too. 
5. Execute the `gulp` command if it's not already running (or restart it if it is).

By following these steps you will not need to add the third party libraries
into your repository and everything will be minified before deployment.

If you are not able to include it as a bower dependency, simply create a new
folder under the
[`main/static/`](https://github.com/gae-init/gae-init/tree/master/main/static)
directory and include them as described in the steps 3—5 above.

> Check out the examples on how to include
[Bootswatch](https://github.com/gae-init/gae-init/pull/360/files),
[Underscore](https://github.com/gae-init/gae-init/pull/438/files) or
[NProgress](https://github.com/gae-init/gae-init/pull/437/files).
