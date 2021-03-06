"""
user models
"""
import json

from google.appengine.ext import ndb


class User(ndb.Model):
    id = ndb.IntegerProperty(required=True)
    title = ndb.StringProperty()
    first_name = ndb.StringProperty()
    last_name = ndb.StringProperty()
    email = ndb.StringProperty()
    profile_picture = ndb.StringProperty()
    member = ndb.BooleanProperty()
    staff = ndb.BooleanProperty()
    account_id = ndb.IntegerProperty()
    addresses = ndb.StringProperty()
    admin_privileges = ndb.JsonProperty()
    inactive = ndb.BooleanProperty()
    inactive_reason = ndb.StringProperty()
    subdomain = ndb.StringProperty()
    church_name = ndb.StringProperty()
    jwt = ndb.StringProperty()

    @classmethod
    def build_key(cls, user_id):
        return ndb.Key(cls, user_id)

    @classmethod
    def put_from_city_dict(cls, city_dict):
        user_key = cls.build_key(city_dict['id'])
        user = user_key.get()
        if not user:
            user = User(key=user_key)
        for attribute, value in city_dict.iteritems():
            if attribute == 'addresses':
                value = json.dumps(value)
            setattr(user, attribute, value)

        return user.put()

    @classmethod
    def get_by_user_id(cls, user_id):
        return cls.build_key(user_id).get()

    def get_key_hash(self):
        """
        For storing the JWT on client side (as a login token)
        """
        return self.jwt

    @property
    def info_dict(self):
        """
        Get a dictionary of basic info about a user
        :r_type: dict
        """
        return {
            'title': self.title,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'profile_picture': self.profile_picture
        }


def get_count_of_users():
    """ Gets the number of user models in the system """
    return User.query().count()
