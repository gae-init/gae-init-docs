First of all since **gae-init** is running on Google App Engine, you will have
to check if the Python library that you are trying to use is compatible.

The easiest way to add a new library is to append it into the
[`requirements.txt`](https://github.com/gae-init/gae-init/blob/master/requirements.txt)
and then execute the `gulp` command if it's not already running. Once installed
you can simply import it in your project as a Python module.

> Check out an example on how to include
[Markdown](https://github.com/gae-init/gae-init/pull/366/files).
