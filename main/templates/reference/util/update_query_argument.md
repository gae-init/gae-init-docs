{% raw %}

Takes the current URL request and updates only the argument `name` with the given `value`. If the value is omitted then that argument will be removed from the request. This function is intended to be used in the Jinja2 templates and currently it's being used in [`utils.order_by_link()`](#utils.order_by_link) and [`utils.filter_by_link()`](#utils.filter_by_link).

##### Arguments

<dl>
  <dt>name</dt>
  <dd>The name of the argument to be updated.</dd>
  <dt>value</dt>
  <dd>
    Optional new value for the given argument. When omitted, the argument
    will be removed if any.
  </dd>
  <dt>ignore</dt>
  <dd>
    Optional list of arguments that will be ignored and removed from the
    generated request. Sometimes it is needed when in the original request the
    <code>cursor</code> is present and it will be invalid if some of the other
    arguments will have a different value.
  </dd>
</dl>

{% endraw %}
