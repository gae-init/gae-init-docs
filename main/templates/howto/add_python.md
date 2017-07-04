Since **gae-init** is running on Google App Engine, the Python library have to
be compatible with App Engine.

The easiest way to add a new library is:

1. Append the library into the
   [`requirements.txt`](https://github.com/gae-init/gae-init/blob/master/requirements.txt).
2. Execute `gulp`, if it's not already running.
3. The newest library will have to appear under `main/lib` directory.
4. Finally import it and use it in the project.

> Check out the example on how to include
[Markdown](https://github.com/gae-init/gae-init/pull/366/files).

You might need to delete `main/lib.zip` file before deploying the new library into GAE.
