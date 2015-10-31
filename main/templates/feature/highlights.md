- JSON services with
  [more URL]({{url_for('api.user.list')}}),
  [limits]({{url_for('api.user.list', limit=8)}}),
  [filters]({{url_for('api.user.list', admin='true')}}),
  [orders]({{url_for('api.user.list', order='name')}}) and
  [more..]({{url_for('api.user.list', limit=4, order='name', admin='true')}})
- JSONP support by providing a
  [`&callback`](http://gae-init.appspot.com{{url_for('api.user.list', limit=2, order='name', callback='hello')}})
  argument to JSON services
- Custom pages for error handlings, like [404](/404)
- Jinja2 template macros for
  [form inputs]({{url_for('feedback')}}),
  [order by links](http://gae-init.appspot.com{{url_for('user_list', order='name')}}),
  [filter by links](http://gae-init.appspot.com{{url_for('user_list', admin=True, active=True, limit=16)}}),
  [easy pagination](http://gae-init.appspot.com{{url_for('user_list', limit=4, active=True, order='-modified')}})
  and more..
- Secret keys and other settings are stored securely in Datastore
- Admin console to manage secret keys and other settings
- Mobile first through Bootstrap 3
- Automatic redirect to where you were after sign-in
- Showing relative time for `<time datetime='...'>`
- Add `.btn-loading` and your buttons will have the loading functionality
- Working [feedback form]({{url_for('feedback')}})
- Multiple OAuth options to [sign-in](https://gae-init.appspot.com/signin/)
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
