{% raw %}

Generates a link that will update only the `&order=` argument of the query to
the correct value depending on the possible sort order that is already applied.
If that particular order is already applied then it will be clearly indicated
with the correct icon.

##### Arguments

<dl>
  <dt>property</dt>
  <dd>The name of the entity's property.</dd>
  <dt>title</dt>
  <dd>
    The title that will appear to the end user.
  </dd>
  <dt>ignore</dt>
  <dd>
    Optional list of arguments that will be ignored and removed from the
    generated request. Sometimes it is needed when in the original request the
    <code>cursor</code> is present and it will be invalid if some of the other
    arguments will have a different value.
  </dd>
</dl>

> #### Examples & Demo
> Check how it is used in
> [user_list.html](https://github.com/gae-init/gae-init/blob/master/main/templates/user/user_list.html)
> and play with orders in
> [User List](https://gae-init.appspot.com/user/?order=-modified).

{% endraw %}
