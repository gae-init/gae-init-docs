- JSON services with
  <a href="http://gae-init.appspot.com{{url_for('user_list_service')}}" target="_blank">more URL</a>,
  <a href="http://gae-init.appspot.com{{url_for('user_list_service', limit=8)}}" target="_blank">limits</a>,
  <a href="http://gae-init.appspot.com{{url_for('user_list_service', admin='true')}}" target="_blank">filters</a>,
  <a href="http://gae-init.appspot.com{{url_for('user_list_service', order='name')}}" target="_blank">orders</a> and
  <a href="http://gae-init.appspot.com{{url_for('user_list_service', limit=4, order='name', admin='true')}}" target="_blank">more..</a>
- JSONP support by providing a
  <a href="http://gae-init.appspot.com{{url_for('user_list_service', limit=2, order='name', callback='hello')}}" target="_blank">`&callback`</a>
  argument to JSON services
- Custom pages for error handlings, like [404](/404)
- Jinja2 template macros for
  [form inputs]({{url_for('feedback')}}),
  <a href="http://gae-init.appspot.com{{url_for('user_list', order='name')}}" target="_blank">order by links</a>,
  <a href="http://gae-init.appspot.com{{url_for('user_list', admin=True, active=True, limit=16)}}" target="_blank">filter by links</a>,
  <a href="http://gae-init.appspot.com{{url_for('user_list', limit=4, active=True, order='-modified')}}" target="_blank">easy pagination</a>
  and more..
- Secret keys and other settings are stored securely in Datastore
- Admin console to manage secret keys and other settings
- Mobile first through Bootstrap 3
- Automatic redirect to where you were after sign-in
- Showing relative time for `<time datetime='...'>`
- Add `.btn-loading` and your buttons will have the loading functionality
- Working [feedback form]({{url_for('feedback')}})
- Multiple OAuth options to [sign-in]({{url_for('signin')}})
  (Google, Facebook, Twitter)
- Add easily any other OAuth provider
- User list that is visible only to the administrators
- Delete or merge users
- User permissions are rout decorators
- Easy pagination with custom wrappers using NDB cursors
- Prefetch links for next pages
- Gravatar support for [user profile]({{url_for('profile')}})
- Secure cookies through Flask's sessions
- HTML5 Rocks
- [This document was successfully checked as HTML5!](http://validator.w3.org/check?verbose=1&uri={{request.host_url[:-1]}}{{request.path}})
- SEO friendly with stuff like [sitemaps.xml]({{url_for('sitemap')}}),
  [robots.txt](/robots.txt) and even a custom [favicon.ico](/favicon.ico)
- Dismissible user notifications in 4 different categories
- Announcement posts across the whole site configurable by administrators
- Many more small details and optimisations
