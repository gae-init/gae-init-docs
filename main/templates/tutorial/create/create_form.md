{% raw %}
There are a few things that we need to do in order to start adding new
contacts. In short we're going to create a Form, a Handler and a Template.

### Contact Create Form
Create a new file `contact.py` in the `main` directory
and add the following code that will be responsible for validating the user's
input.

    from flask.ext import wtf

    class ContactUpdateForm(wtf.Form):
    name = wtf.StringField('Name', [wtf.validators.required()])
    email = wtf.StringField('Email', [wtf.validators.optional(), wtf.validators.email()])
    phone = wtf.StringField('Phone', [wtf.validators.optional()])
    address = wtf.TextAreaField('Address', [wtf.validators.optional()])

For more information regarding the form validation refert to
[Flask-WTForms](http://flask.pocoo.org/docs/patterns/wtforms/).

### Contact Create Handler

After creating the form we have to create a handler for it. Add the
following code into the `contact.py` file.

    import flask
    import auth
    import model
    from main import app

    @app.route('/contact/create/', methods=['GET', 'POST'])
    @auth.login_required
    def contact_create():
    form = ContactUpdateForm()
    if form.validate_on_submit():
      contact_db = model.Contact(
          user_key=auth.current_user_key(),
          name=form.name.data,
          email=form.email.data,
          phone=form.phone.data,
          address=form.address.data,
        )
      contact_db.put()
      return flask.redirect(flask.url_for('welcome'))
    return flask.render_template(
        'contact_create.html',
        html_class='contact-create',
        title='Create Contact',
        form=form,
      )


#### Let's take a closer look in this new snippet

    import flask
    import auth
    import model
    from main import app

The nessesary imports for creation handler, just put
them in the beginning of the `contact.py` file with the rest of the
imports.

    @app.route('/contact/create/', methods=['GET', 'POST'])

The route and the methods that we are going to use.
`GET` is to serve the html form and `POST` is to
submit the data.

For more information refert to Flask documentation on
[routing](http://flask.pocoo.org/docs/quickstart/#routing).

    @auth.login_required

This decorator's purpose is to make sure that who ever is entering
this URL will be already signed in so we could use the `user_key`
of the authentiacated user. If the user is not logged in, she will be
redirected to the signin page and then back to this URL.

{% endraw %}
