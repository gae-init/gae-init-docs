So after wetting your appetite in the [Tutorial]({{url_for('tutorial')}}) we
will now give you the big picture overview of the gae-init environment. After
reading this guide you should understand how the individual blocks of gae-init
play together, how you can benefit most of them and where to start in case you
want to customize things.



Overview { #overview }
--------
- [interplay of components](#interplay)
    - [run.py](#run_py)
    - [config.py](#config_py)
    - [appcfg & app.yaml](#appengine)
    - [server side tasks](#server_side_tasks) (setup, compiling, minification, bundling)
        - [node](#node)
        - [grunt](#grunt)
        - [bower](#bower)
        - [livereload](#livereload)
        - [coffee](#coffee)
        - [lesscss](#lesscss)
    - [server side libs](#server_side_libs) (python)
    - [client side libs](#client_side_libs) (js)
- [main.py](#main_py)
- [templates/base.html](#templates_base)
    - [available blocks](#templates_blocks)
    - [bits](#templates_bits) (especially style + js)
- [Frequent tasks / dev workflows](#workflows)
    - [running the server](#run_dev_server)
    - [customize styles](#custom_styles)
    - [custom javascript / coffeescript](#custom_js)
    - [add a new python lib](#new_python_lib)
    - [add a new js lib](#new_js_lib) (bower)
    - [add a new page](#new_page)


To be done:
===========


interplay of components { #interplay }
--------------------------------------
{{"###"}} run.py { #run_py }

{{"###"}} config.py { #config_py }

{{"###"}} appcfg & app.yaml { #appengine }

{{"###"}} server side tasks (setup, compiling, minification, bundling) { #server_side_tasks }

{{"####"}} node { #node }

{{"####"}} grunt { #grunt }

{{"####"}} bower { #bower }

{{"####"}} livereload { #livereload }

{{"####"}} coffee { #coffee }

{{"####"}} lesscss { #lesscss }

{{"###"}} server side libs (python) { #server_side_libs }

{{"###"}} client side libs (js) { #client_side_libs }



main.py { #main_py }
--------------------



templates/base.html { #templates_base }
---------------------------------------

{{"###"}} available blocks { #templates_blocks }

{{"###"}} bits (especially style + js) { #templates_bits }



Frequent tasks / dev workflows { #workflows }
---------------------------------------------

{{"###"}} running the server { #run_dev_server }

{{"###"}} customize styles { #custom_styles }

{{"###"}} custom javascript / coffeescript { #custom_js }

{{"###"}} add a new python lib { #new_python_lib }

{{"###"}} add a new js lib (bower) { #new_js_lib }

{{"###"}} add a new page { #new_page }

