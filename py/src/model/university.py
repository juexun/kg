from py2neo.ogm import GraphObject, Property, RelatedTo, RelatedFrom

class University(GraphObject):

    __primarykey__ = "name"

    name = Property()

    specialities = RelatedFrom("University", "专业")
    colleges = RelatedFrom("Unversity", "学院")