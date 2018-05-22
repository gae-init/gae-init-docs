{% raw %}

In order to update the contact we will have to do three things: create the handler that will retrieve the contact from the datastore, the template to update her in the browser and the link on the contact list for easy access.

In this step there are very similar actions on what we have to do that we've seen in creation and viewing of the contact. So in the final step we'll combine the create and update templates to maintain only one.

### Contact Update Handler

Add the following code to the `contact.py` file:

```python
@app.route('/contact/<int:contact_id>/update/', methods=['GET', 'POST'])
@auth.login_required
def contact_update(contact_id):
  contact_db = model.Contact.get_by_id(contact_id)
  if not contact_db or contact_db.user_key != auth.current_user_key():
    flask.abort(404)
  form = ContactUpdateForm(obj=contact_db)
  if form.validate_on_submit():
    form.populate_obj(contact_db)
    contact_db.put()
    return flask.redirect(flask.url_for('contact_list', order='-modified'))
  return flask.render_template(
      'contact_update.html',
      html_class='contact-update',
      title=contact_db.name,
      form=form,
      contact_db=contact_db,
    )
```

### Contact Update Template

After the handler, we are going to need a template to be able to update the user's details. Create a new file `contact_update.html` in the `templates` directory and paste the following code there:

```html
# extends 'base.html'
# import 'macro/forms.html' as forms

# block content
  <div class="page-header">
    <h1>{{title}}</h1>
  </div>
  <div class="row">
    <div class="col-md-4">
      <form method="POST" action=".">
        <fieldset>
          {{form.csrf_token}}
          {{forms.text_field(form.name, autofocus=True)}}
          {{forms.email_field(form.email)}}
          {{forms.text_field(form.phone)}}
          {{forms.textarea_field(form.address)}}
          <button type="submit" class="btn btn-primary btn-block">
            Update Contact
          </button>
        </fieldset>
      </form>
    </div>
  </div>
# endblock
```

### Finalise Contact Update

As a final touch we're going to do two things: add some links to the contact list to access the update contacts page easier and also we'll get rid of the `contact_create.html` because it is very similar to the `contact_update.html`.

#### Add a link on the contact list

Find the line that renders the ID of the contact and replace it with the following:

```html
...
<td>
  <a href="{{url_for('contact_update', contact_id=contact_db.key.id())}}">
    {{contact_db.key.id()}}
  </a>
</td>
...
```

Now visit the contact list ([http://localhost:3000/contact/](http://localhost:3000/contact/)), and you should be able to click on the ID of each contact and update their properties.

#### Get rid of contact_create.html

At the moment the only difference between the `contact_create.html` and the `contact_update.html` files is the caption of the submit form. Just delete the `contact_create.html` form and change the button in `contact_update.html` to the following:

```html
...
<button type="submit" class="btn btn-primary btn-block">
  # if contact_db
    Update Contact
  # else
    Create Contact
  # endif
</button>
...
```

Finally since we deleted the `contact_create.html` we'll have to simply update the create handler to render the correct template and by now you should be able to find that yourself.

{% endraw %}
