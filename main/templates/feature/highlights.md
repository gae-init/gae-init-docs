<ul>
  <li>
    JSON services with
    <a href="http://gae-init.appspot.com{{url_for('user_list_service')}}" target="_blank">more URL</a>,
    <a href="http://gae-init.appspot.com{{url_for('user_list_service', limit=8)}}" target="_blank">limits</a>,
    <a href="http://gae-init.appspot.com{{url_for('user_list_service', admin='true')}}" target="_blank">filters</a>,
    <a href="http://gae-init.appspot.com{{url_for('user_list_service', order='name')}}" target="_blank">orders</a> and
    <a href="http://gae-init.appspot.com{{url_for('user_list_service', limit=4, order='name', admin='true')}}" target="_blank">more..</a>
  </li>
  <li>
    JSONP support by providing a
    <a href="http://gae-init.appspot.com{{url_for('user_list_service', limit=2, order='name', callback='hello')}}" target="_blank"><code>&amp;callback</code></a>
    argument to JSON services
  </li>
  <li>Custom pages for error handlings, like <a href="/404">404</a></li>
  <li>
    Jinja2 template macros for
    <a href="{{url_for('feedback')}}">form inputs</a>,
    <a href="http://gae-init.appspot.com{{url_for('user_list', order='name')}}" target="_blank">order by links</a>,
    <a href="http://gae-init.appspot.com{{url_for('user_list', admin=True, active=True, limit=16)}}" target="_blank">filter by links</a>,
    <a href="http://gae-init.appspot.com{{url_for('user_list', limit=4, active=True, order='-modified')}}" target="_blank">easy pagination</a>
    and more..
  </li>
  <li>Secret keys and other settings are stored securely in Datastore</li>
  <li>Admin console to manage secret keys and other settings</li>
  <li>Mobile first through Bootstrap 3</li>
  <li>Automatic redirect to where you were after sign-in</li>
  <li>Showing relative time for <code>&lt;time datetime='...'&gt;</code></li>
  <li>Add <code>.btn-loading</code> and your buttons will have the loading functionality</li>
  <li>Working <a href="{{url_for('feedback')}}">feedback form</a></li>
  <li>Multiple OAuth options to <a href="{{url_for('signin')}}">sign-in</a> (Google, Facebook, Twitter)</li>
  <li>Add easily any other OAuth provider</li>
  <li>User list that is visible only to the administrators</li>
  <li>Delete or merge users</li>
  <li>User permissions are rout decorators</li>
  <li>Easy pagination with custom wrappers using NDB cursors</li>
  <li>Prefetch links for next pages</li>
  <li>Gravatar support for <a href="{{url_for('profile')}}">user profile</a></li>
  <li>Secure cookies through Flask's sessions</li>
  <li>HTML5 Rocks</li>
  <li><a href="http://validator.w3.org/check?verbose=1&amp;uri={{request.host_url[:-1]}}{{request.path}}">This document was successfully checked as HTML5!</a></li>
  <li>SEO friendly with stuff like <a href="{{url_for('sitemap')}}">sitemaps.xml</a>, <a href="/robots.txt">robots.txt</a> and even <a href="/favicon.ico">favicon.ico</a></li>
  <li>Dismissible user notifications in 4 different categories</li>
  <li>Announcement posts across the whole site configurable by admininistrators</li>
  <li>Many more small details and optimizations</li>
</ul>
