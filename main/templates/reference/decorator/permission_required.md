If you need more fine-grained control over who can access what, you can use
the `@auth.permission_required(permission)` decorator. It will only
allow accesses to the decorated function by registered users who were given
that permission (or admins). It works like this:


```python
@app.route('/moderate')
@auth.permission_required('moderator')
def moderate():
  return flask.render_template(...)
```

This will automagically register `'moderator'` as an available
permission which an admin can assign to individual users via the user list.
For convenience you can leave the `permission` string empty, which
will cause the permission to  named as the decorated function (so
`@auth.permission_required()` would introduce and check for the
permission `'moderate'` in the example above).

If `methods` is specified, the decorator will only enforce the given
permission for requests with a method as in `methods`
(e.g., `@auth.permission_required('foo_w', methods=['POST'])` will
only check the user for permission `'foo_w'` in POST requests
but won't restrict other requests).
If `methods` is `None` (default), the permissions will be enforced
on all requests regardless of their method.

Several uses of this decorator can be combined as in the example below.
This only allows access to `endpoint` in GET requests if the user has `'foo_r'`
permission. For POST requests the user needs both `'foo_r'` and `'foo_w'`:

```python
@app.route('/endpoint/')
@auth.permission_required('foo_r')
@auth.permission_required('foo_w', methods=['POST'])
def endpoint():
  pass
```

Typical usecases:

 - allow everyone to read, restrict write to a few users: just leave out the
   second line
 - allow all logged in users to read, restrict write to a few users: replace the
   second line with `@auth.login_required`

The order of the statements is not important as the permissions
are wrapped around each other. All of the permission guards have to
be passed in order to reach `endpoint`. Passing one of them does
**not** skip the others.
