{% raw %}
### Finalise Contact Creation

Before we can actually test the contact creation there are couple of things
that we have to complete.

#### Import contact.py

We will have to import the <code>contact.py</code> in the <code>main.py</code>,
because otherwise the Flask application won't be able to figure out the
routing rules. Include the following line bellow the rest of the imports
in the `main.py` file.

    import contact

#### Adding a link on the top bar

The most important thing to make the user experience better, we will have
to create a link for the users to be able to start adding new contacts
in their phonebook.
Add the lines `2 - 4` inside the
`<ul class="nav">...</ul>` element that you will find in the
`header.html` file that is located in the
`templates/bit` directory.

    <ul class="nav navbar-nav">
      <li class="{{'active' if html_class == 'contact-create'}}">
        <a href="{{url_for('contact_create')}}"><i class="fa fa-file"></i> Create Contact</a>
      </li>
      ...
    </ul>

### Testing Contact Creation

If your development server is still running, then by visting the
[http://localhost:8080/](http://localhost:8080/)
you should notice the Create Contact link on the top bar and you should be able
to actually start creating new contacts!

Create couple of new contacts and also try to add a contact without
a name, or try to enter an invalid email and then press on **Create Contact**
button.

Since the contact list is not visible in the application yet, you can
visit the Google App Engine's admin console to make sure that the
contacts are being added, by visiting the admin console:
[http://localhost:8081/datastore](http://localhost:8081/datastore?kind=Contact).

{% endraw %}
