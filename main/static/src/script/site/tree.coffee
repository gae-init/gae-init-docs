window.init_tree = () ->

  $('.file').each () ->
    $link = $(this)
    if tooltips[$link.attr('id')]
      $link.attr('data-toggle', 'popover')
      $link.attr('data-html', 'true')
      $link.attr('data-content', tooltips[$link.attr('id')])
      $link.attr('data-placement', 'right')
      $link.attr('data-title', $link.text())
      $link.popover()
    else
      $link.addClass('text-muted')


  ($ 'body').on 'click', '.file', (e) ->
    $('.file').popover('hide')
    $(this).popover('show')
    e.stopPropagation()


  $('body').click () ->
    $('.file').popover('hide')


tooltips =
  'gae-init': 'The project parent directory.'
  'README.md': 'The small introduction and the description of the project.'
  'main': 'This is where the main Google App Engine lives. Whatever has to do with it, should go in this directory.'
  'admin.py': 'The handler for the administrative configuration of the application.'
  'auth.py': 'Authenticated user related handlers, functions and decorators. <a href="/reference#auth">Read more</a>'
  'run.py': 'The run script that among other things also comiples and minifies *.less and *.coffee files. <hr>Run <code>./run.py -h</code> for more.'
  'config.py': 'Global configuration contstants. <hr> <a href="/reference#config">Read more</a>'
  'main.py': 'The main entry point and where the majority of the handlers are defined. For bigger projects the handlers should be splitted in different files.'
  'model.py': 'The models for the application.'
  'modelx.py': 'The extended properties for the models.'
  'util.py': 'Extra utilities to help you with the stuff <hr> <a href="/reference#util">Read more</a>'

  'app.yaml': 'The Python Application Configuration file. <hr> <a href="https://developers.google.com/appengine/docs/python/config/appconfig" target="_blank">Read More <i class=" icon-external-link"></i></a>'
  'package.json': 'The dependencies that needs to be installed via npm: CoffeeScript, LESS, UglifyJS, Grunt.'

  'static': 'All the static files, including images, scripts, stylesheets, front end libraries and more. If it is not Python related then most likely it goes into this directory.'
  'favicon.ico': 'Update this file with your own favicon.ico.'
  'robots.txt': 'List of pages that you would like to hide from the web crawlers.'
  'static-lib': 'All the client side libraries, usually going to this folder. Stuff like jQuery, jQuery Plugins, Bootstrap, etc.'
  'font-awesome': 'The Font Awesome stylesheets that are used to replace the default Glpyhicons that are bundled with Bootstrap.'
  'jquery.js': 'The latest unminified jQuery library, but it is minified before deployment.'

  'font': 'All the custom fonts.'
  'img': 'All the static images.'

  'dst': 'The auto generated directory that contains the compiled scripts and stylesheets, that are used when running on local server.'
  'min': 'The auto generated directory that contains the compiled, minified and uglified scripts and stylesheets, that are used when running on remote server.'

  'lib': 'The server side (Python) libraries. If you want to add more Python libraries that are not included in the default installation, just put them here.'
  'bootstrap': 'The Bootstrap sources that includes all the *.less and *.js files.'
  'moment.js': 'A javascript date library for parsing, validating, manipulating, and formatting dates. <hr> <a href="http://momentjs.com/" target="_blank">Read More <i class=" icon-external-link"></i></a>'

  'templates': 'The Jinja2 templates.'
  'base.html': 'The base template that most of the pages are inheriting from.'
  'error.html': 'The user friendly error template'
  'analytics.html': 'The Google Analytics code. It renders only if the Analytics ID is present and the signed in user is not an administrator.'
  'profile.html': 'The update user profile form from.'
  'feedback.html': 'The send feedback from.'
  'signin.html': 'The sign in page with different options.'
  'header.html': 'Top navigation header.'
  'footer.html': 'The footer that shows the copyright info, version and more.'

  'admin': 'The admin related templates should go here.'
  'config_update.html': 'The update form for the configuration of the application.'

  'bit': 'Small snippets of HTML templates.'
  'form_select_field.html': 'The <code>&lt;select&gt;</code> element for the <code>&lt;form&gt;</code>. Takes as parameter Flask-WTF form field.'
  'form_text_field.html': 'The <code>&lt;input&gt;</code> element for the <code>&lt;form&gt;</code>. Takes as parameter Flask-WTF form field.'
  'form_textarea_field.html': 'The <code>&lt;textarea&gt;</code> element for the <code>&lt;form&gt;</code>. Takes as parameter Flask-WTF form field.'
  'user_list.html': 'The list of users of the application.'
  'welcome.html': 'The front page of the application.'
  'script.html': 'The the JavaScript includes of the application.  Takes advantage of the build script to deliver different styles depending on where the application runs.'
  'style.html': 'The stylesheets of the application. Takes advantage of the build script to deliver different styles depending on where the application runs.'
  'notifications.html': 'The flash notifications that appearing as alerts on top of the pages.'
  'user_menu.html': 'The top navigations drop down menu for the authenticated user.'
