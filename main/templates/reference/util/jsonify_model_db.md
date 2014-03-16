{% raw %}

Returns a JSON (or JSONP if the `&callback` argument is present) Response of a
single entity object. The returned JSON object has 3 properties: `status` which
is always **"success"**, `now` which shows the UTC time in ISO format and
`result` which contains the serialised version of the given entity.

##### Arguments

<dl>
  <dt>model_db</dt>
  <dd>The single entity object to be returned as JSON or JSONP</dd>
</dl>

{% endraw %}
