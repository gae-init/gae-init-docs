{% raw %}

The `User` entity model of the authenticated user if there is one, otherwise `None`. If you want to make sure that this function will return a `user_db` use one of the [decorators](#decorator).

In templates you can get access to this variable through `{{current_user.user_db}}`. So if you would like to display the name of the currently signed in user somewhere you would use it like: `{{current_user.user_db.name}}`.

{% endraw %}
