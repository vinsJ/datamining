import rdflib

g = rdflib.Graph()

# ... add some triples to g somehow ...
g.load("./Lyon/Lyon.rdf")

qres = g.query(
    """SELECT DISTINCT ?x ?y ?z
       WHERE {
           ?x ?y ?z
       }""")

for row in qres:
    print(row)