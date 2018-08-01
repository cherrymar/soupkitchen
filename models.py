from google.appengine.ext import ndb

class Restuarant(ndb.Model):
    name = ndb.StringProperty(required=False)
    location = ndb.StringProperty(required=False)
    id = ndb.IntegerProperty(required=False)
    num_servings = ndb.IntegerProperty(required=False)
    types_of_food = ndb.StringProperty(repeated=False)

class Food(object):
    def __init__(self):
        self.name = name
        self.ingredients = ingredients
        


class Shelter(ndb.Modle):
    name =
    location =
    num_occupants =
    num_chosen =
    reservations =
