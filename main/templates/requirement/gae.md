Download and install the
[Google Cloud SDK](https://developers.google.com/cloud/sdk/). Afterwards, since
App Engine SDK is not included in the default package, install it via:

```bash
$ gcloud components install app-engine-python
```

After the installation make sure that you are able to run
[the Python Development Server](https://developers.google.com/appengine/docs/python/tools/devserver)
from the terminal: `dev_appserver.py --help`.
