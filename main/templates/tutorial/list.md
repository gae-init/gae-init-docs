{% raw %}

In order to present the contacts we will have to do three things: create the handler that will retrieve the contacts from the datastore, the template to present them in the browser and the link on the top bar to access this list.

### Contact List Handler

Add the following code to the `contact.py` file:

```python
import util

@app.route('/contact/')
@auth.login_required
def contact_list():
  contact_dbs, contact_cursor = model.Contact.get_dbs(
      user_key=auth.current_user_key(),
    )

  return flask.render_template(
      'contact_list.html',
      html_class='contact-list',
      title='Contact List',
      contact_dbs=contact_dbs,
      next_url=util.generate_next_url(contact_cursor),
    )
```

### Contact List Template

After creating the handler, we are going to need a template to be able to present a table of all the contacts that we've added so far. Create a new file `contact_list.html` in the `templates` directory and paste the following code there:

```html
# extends 'base.html'

# block content
  <div class="page-header">
    <h1>{{title}}</h1>
  </div>
  <table class="table table-bordered">
    <thead>
      <tr>
        <th>ID</th>
        <th>Name</th>
        <th>Email</th>
        <th>Phone</th>
        <th>Address</th>
      </tr>
    </thead>
    <tbody>
      # for contact_db in contact_dbs
        <tr>
          <td>{{contact_db.key.id()}}</td>
          <td>{{contact_db.name}}</td>
          <td>{{contact_db.email}}</td>
          <td>{{contact_db.phone}}</td>
          <td>{{contact_db.address}}</td>
        </tr>
      # endfor
    </tbody>
  </table>
# endblock
```

You can test the handler and the above template by visiting the url [http://localhost:3000/contact/](http://localhost:3000/contact/), but in the next section we'll add a link to make it easier to access.

### Finalise Contact Listing

As a final touch we're going to do two things: adding the link in the top bar and changing the redirect after creating the contact to take us to the this list instead of going back to the welcome page.

#### Adding a link on the top bar

Add the lines `3 - 5` inside the `<ul class="nav navbar-nav">...</ul>` element that you will find in the `header.html` file that is located in the `templates/bit` directory.

```html
<ul class="nav navbar-nav">
  ...
  <li class="{{'active' if html_class == 'contact-list'}}">
    <a href="{{url_for('contact_list')}}"><i class="fa fa-list"></i> Contact List</a>
  </li>
  ...
</ul>
```

After refreshing the page ([http://localhost:3000/](http://localhost:3000/)), you should be able to see the link on the top and if you're in watching the contact list it should also be `active`.

#### Changing the redirect

After creating a new contact we will now redirect the user to the contact list instead of the welcome page and also and also show her a message that the new contact was successfully created.

Find the following line in the contact_create handler:

```python
return flask.redirect(flask.url_for('welcome'))
```

and replace it with the following:

```python
flask.flash('New contact was successfully created!', category='success')
return flask.redirect(flask.url_for('contact_list', order='-created'))
```

The first line is to flash the message that the creation was successful. The argument `category` is optional and can be one of the following: `warning` (default), `danger`, `success` or `info`.

In the second line notice that we are using the `order='-created'` in the `url_for` function, which will be translated to: [http://localhost:3000/contact/?order=-created](http://localhost:3000/contact/?order=-created). You can choose whatever order you like and you can also play with the url by providing different orders for the fields that you have in the `Contact` model. Use the `-` if you want the inverse order and `,` to combine more than one field for order.

{% endraw %}
