We assume that you already know how to run the Google App Engine
applications from a command line, but if not you should refer to the
[documentation](https://developers.google.com/appengine/docs/python/gettingstartedpython27/helloworld).
Execute in your terminal the `run.py` from the root directory

```bash
$ cd /path/to/phonebook
$ ./run.py -s
```

If everything went smoothly you can test the application by visiting the
following URL in your web browser:

[http://localhost:8080/](http://localhost:8080/)

Feel free to spend some time by clicking on the different menus. As a first
change within the app you can sign in as administrator and after visiting the
[http://localhost:8080/admin/config/](http://localhost:8080/admin/config/)
change the **Brand Name** from **gae-init** to **Phonebook** (or to
anything else you like). By doing that you should see on the top left corner
the new name for your application.
