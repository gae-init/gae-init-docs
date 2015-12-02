Executing the `gulp` command to start the local server andall the watchers. If
everything went OK, visit the [http://localhost:8080](http://localhost:8080).

All the custom styles are located in
[`main/static/src/style/`](https://github.com/gae-init/gae-init/tree/master/main/static/src/style)
directory and you update them if needed. Most of the times though is much better
to create a new file or files for better structure of your prject. Here is how:

  1. Create a new file under `main/static/src/style/` called `foo.less`.
  2. Open the `base.less` and append `@import "foo";` at the end.

From now on, you can simply start adding new styles in the `foo.less` file and
your page will automatically refresh to reflect the changes.
