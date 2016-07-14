The `@auth.cron_required` decorator is used to enforce access
constraints on an endpoint used for scheduled tasks.

This decorator checks for the presence of the `X-Appengine-Cron: true`
header that GAE automatically adds to a scheduled task request.

It also checks for admin permissions, which allows for testing of
scheduled tasks.

For more information on how to create scheduled tasks in GAE, see
[Scheduling Tasks With Cron for Python](https://cloud.google.com/appengine/docs/python/config/cron)
