from py2neo.ogm import GraphObject, Property, RelatedTo

class Person(GraphObject):

    __primarykey__ = "name"

    name = Property()
    sex = Property()
    born = Property()
    education = Property()
    nationality = Property()
