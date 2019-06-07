from rdflib import Graph, URIRef, BNode, Literal, Namespace
from rdflib.namespace import RDF, FOAF, SKOS

ns = Namespace("http://gzsunrun.cn/company/0.1/employee/")
bob_name = Literal('Bob')


g = Graph()

g.add( (ns.bob, RDF.type, FOAF.Person) )
g.add( (ns.bob, FOAF.name, Literal('Bob')) )
g.add( (ns.bob, FOAF.knows, ns.linda) )
g.add( (ns.linda, RDF.type, FOAF.Person) )
g.add( (ns.linda, FOAF.name, Literal('Linda') ) )

g.serialize(destination="demo.ttl", format='ttl')

# g = Graph()
# g.parse("http://xmlns.com/foaf/spec/index.rdf")
# for sub in g.subjects():
#     print(sub)

# for obj in g.objects():
#     print(obj)

for pred in g.predicates():
    print(pred)

# for so in g.subject_objects():
#     print(so)

# for node in g.all_nodes():
#     print(type(node), node)