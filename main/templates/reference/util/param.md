{% raw %}

Returns the value of the requested argument either via a URL argument or through the input element of a form. If the requested parameter is not provided this function will return `None`.

##### Arguments

<dl>
  <dt>name</dt>
  <dd>The name of the argument or the form's input name.</dd>
  <dt>cast</dt>
  <dd>
    Type of the argument that the param should be casted to. If you want to
    cast to a <code>bool</code> it will return <code>True</code> to any of
    these values: <code>true</code>, <code>yes</code> or <code>1</code>.
  </dd>
</dl>

{% endraw %}
