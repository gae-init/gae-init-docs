{% raw %}
A bunch of configuration variables are already being stored in our datastore
and they are available globally across the app. If you want to get the
`brand_name` in Python you can access it with `config.CONFIG_DB.brand_name`
and from HTML files via Jinja2 `{{config.CONFIG_DB.brand_name}}`.

If you want to add something new, start by adding a property in our `Config`
model that is located in `main/model/config.py`:

```python
foo = ndb.IntegerProperty(default=0)
```

..afterwards find the `ConfigUpdateForm` in the `main/control/admin.py` and
something like:

```python
foo = wtforms.IntegerField(model.Config.foo._verbose_name)
```

..finally add the following to template `templates/admin/admin_config.html`:

```html
{{forms.number_field(form.foo)}}
```

By visiting the [localhost:8080/admin/config/](http://localhost:8080/admin/config/)
you will be able to edit the new property.
{% endraw %}
