{% raw %}

Generates a link that will add (or replace) <code>&property=value</code> to the current request or will remove it if it's already there. Optionally instead of showing the actual value it is possible to show an icon. The icon is more appropriate when filtering by boolean properties.

##### Arguments

<dl>
  <dt>property</dt>
  <dd>The name of the entity's property.</dd>
  <dt>value</dt>
  <dd>
    The value to be applied to the filter.
  </dd>
  <dt>icon</dt>
  <dd>
    Optional name for the icon instead that will be shown instead of the value.
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
>
> Check how it is used in [user_list.html](https://github.com/gae-init/gae-init/blob/master/main/templates/user/user_list.html) and play with filters in [User List](https://gae-init.appspot.com/user/?order=-modified).

{% endraw %}
