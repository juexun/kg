from rdflib import Graph, URIRef, BNode, Literal, Namespace
from rdflib.namespace import RDF, FOAF

ns = Namespace("http://gzsunrun.cn/company/0.1/employee/")
bob_name = Literal('Bob')


g = Graph()

g.add( (ns.bob, RDF.type, FOAF.Person) )
g.add( (ns.bob, FOAF.name, Literal('Bob')) )
g.add( (ns.bob, FOAF.knows, ns.linda) )
g.add( (ns.linda, RDF.type, FOAF.Person) )
g.add( (ns.linda, FOAF.name, Literal('Linda') ) )

g.serialize(destination="demo.ttl", format='turtle')