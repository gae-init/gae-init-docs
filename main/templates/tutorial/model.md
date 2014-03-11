As we are building a personal phonebook, we'll need to add the contact list.
Add the following at the end of `model.py`:

    class Contact(Base):
      user_key = ndb.KeyProperty(kind=User, required=True)
      name = ndb.StringProperty(required=True)
      email = ndb.StringProperty(default='')
      phone = ndb.StringProperty(default='')
      address = ndb.StringProperty(default='')

The `user_key` property will store the `User`'s key to
make the contact list personal for every user. The rest of the properties are
self explanatory.
