As we are building a personal phonebook, we are going to need to store the contact list in a datastore.

Create a new file called `contact.py` in the `main/model` directory with the following contents:

```python
from google.appengine.ext import ndb
import model

class Contact(model.Base):
  user_key = ndb.KeyProperty(kind=model.User, required=True)
  name = ndb.StringProperty(required=True)
  email = ndb.StringProperty(default='')
  phone = ndb.StringProperty(default='')
  address = ndb.StringProperty(default='')
```

The `user_key` property will store the `User`'s key to make the contact list personal for every user. The rest of the properties are self explanatory.

Finally import it in the `main/model/__init__.py` file like this:

```python
from .contact import Contact
```
