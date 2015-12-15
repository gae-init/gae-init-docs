{% raw %}

Same as [`flask.jsonify()`](http://flask.pocoo.org/docs/api/#flask.json.jsonify),
which means it creates a Response with the JSON representation of the given
arguments with an *application/json* mimetype. The arguments to this function
are the same as to the **dict** constructor.

In addition if `callback` argument is provided in the request then it will
return a response with the JSONP representation.


> #### Demo
> Visit the following URL to check it in action:
> [https://gae-init.appspot.com/_s/user/?callback=foo](https://gae-init.appspot.com/_s/user/?callback=foo)

{% endraw %}
