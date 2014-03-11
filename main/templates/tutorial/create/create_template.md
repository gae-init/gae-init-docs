{% raw %}
### Contact Create Template

After creating the form and a handler, we are going to need a template
to be able to get the user data. Create a new file
<code>contact_create.html</code> in the <code>templates</code> directory
and paste the following code there:

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
            Create Contact
          </button>
        </fieldset>
      </form>
    </div>
  </div>
# endblock
```
{% endraw %}
