from google.appengine.ext import ndb

class Restuarant(ndb.Model):
    name = ndb.StringProperty(required=False)
    location = ndb.StringProperty(required=False)
    id = ndb.IntegerProperty(required=False)
    foods_available = ndb.StringProperty(repeated=True) #save id's of food here
    password = ndb.StringProperty(required=True)


class Food(ndb.Model):
    id = ndb.IntegerProperty(required=False)
    name = ndb.StringProperty(required=False)
    ingredients = ndb.StringProperty(repeated=True)


class Shelter(ndb.Modle):
    name = ndb.StringProperty(required=False)
    location = ndb.StringProperty(required=False)
    occupants = ndb.StringProperty(repeated=True) #save id's of people here


class People(ndb.Model):
    id = ndb.IntegerProperty(required=False)
    name = ndb.StringProperty(required=False)
    age = ndb.IntegerProperty(required=False)
    weight = ndb.IntegerProperty(required=False)
