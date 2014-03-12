Before deploying your application you must minify and uglify your styles
and scripts because otherwise your latest changes won't appear online!

To minify your styles and scripts execute the `run.py` script by
providing the `-m` argument

    $ ./run.py -m

After that make sure that you have created a new application on
[App Engine](http://appengine.google.com)
and the name of the application is updated in the `app.yaml`
file that is located in the `main` directory.

To deploy your application execute the following command from the
root directory:

    $ appcfg.py update main

Test your application by adding new contacts online!
