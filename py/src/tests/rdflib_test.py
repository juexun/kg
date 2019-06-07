import rdflib
g=rdflib.Graph()
g.load('demo.ttl', format="ttl")

for s,p,o in g:
    print(s, p, o)