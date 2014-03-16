Sends an email notification to the feedback email if it set in the admin
config settings. The email is sent as a background task, using the
[deferred](https://developers.google.com/appengine/articles/deferred)
library, to avoid possible errors that could be produced due to quota limits
or anything else. The brand name of the application will be be also used as a
name of the sender and also prefixed to the subject of the email.
