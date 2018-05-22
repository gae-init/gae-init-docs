Execute the `gulp` command to start the local server and all the watchers. If everything went OK, visit [http://localhost:3000](http://localhost:3000).

All the custom styles are located under [`main/static/src/style/`](https://github.com/gae-init/gae-init/tree/master/main/static/src/style) directory and you can update them if needed. Most of the time though it is much better to create more files for better structure of the project. Here is how:

1. Create a new file under `main/static/src/style/` called `foo.less`.
2. Open the `style.less` and append `@import "foo";` at the end.

From now on, you can simply start adding new rules in the `foo.less` file and your web app will automatically refresh to reflect the changes.
