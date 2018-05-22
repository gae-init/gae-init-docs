{% raw %} In order to view the contact we will have to do three things: create the handler that will retrieve the contact from the datastore, the template to view her in the browser and the link on the contact list for easy access.

### Contact View Handler

Add the following code to the `contact.py` file:

```python
@app.route('/contact/<int:contact_id>/')
@auth.login_required
def contact_view(contact_id):
  contact_db = model.Contact.get_by_id(contact_id)
  if not contact_db or contact_db.user_key != auth.current_user_key():
    flask.abort(404)
  return flask.render_template(
      'contact_view.html',
      html_class='contact-view',
      title=contact_db.name,
      contact_db=contact_db,
    )
```

### Contact View Template

After creating the handler, we are going to need a template to be able to present a contact's personal page. Create a new file `contact_view.html` in the `templates` directory and paste the following code there:

```html
# extends 'base.html'

# block content
  <div class="page-header">
    <h1>{{title}}</h1>
  </div>
  <p>{{contact_db.email}}</p>
  <p>{{contact_db.phone}}</p>
  <p>{{contact_db.address}}</p>
  <hr>
  <p>
    <a href="{{url_for('contact_list')}}">Back</a>
  </p>
# endblock
```

It's hard to test this form right now because we have to create manually the URL, but in the next section we'll add a link to make it easier to access.

### Finalise Contact View

As a final touch in order to view the contacts we'll modify the contact list so when you click on their names you should be able to view them.

Find the line that renders the name of the contact and replace it with the following:

```html
...
<td>
  <a href="{{url_for('contact_view', contact_id=contact_db.key.id())}}">
    {{contact_db.name}}
  </a>
</td>
...
```

Now visit the contact list ([http://localhost:3000/contact/](http://localhost:3000/contact/)), and you should be able to click on the name of each contact and view their properties.

{% endraw %}
