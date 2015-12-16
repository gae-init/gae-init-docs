First of all since **gae-init** is running on Google App Engine, you will have
to check if the Python library that you are using is compatible.

The easiest way to add a new library is:

1. Append the library into the
   [`requirements.txt`](https://github.com/gae-init/gae-init/blob/master/requirements.txt).
2. Execute the `gulp` command if it's not already running.
3. When installed you can import it in your project as a Python module.

> Check out the example on how to include
[Markdown](https://github.com/gae-init/gae-init/pull/366/files).
