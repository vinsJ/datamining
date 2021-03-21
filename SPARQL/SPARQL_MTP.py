import rdflib

import rdflib 
from rdflib.plugins.sparql import prepareQuery

qres = prepareQuery(
    """
    SELECT DISTINCT  ?name ?cord ?trans
       WHERE {
        ?x ?z ?w .
        ?w ?c ?name .
        ?w ?t ?trans .
        ?w ?co ?g .
        ?g ?h ?cord

       }
       """)
g = rdflib.Graph()
#Nantes
#Lille
#IDF
g.load("./MTP/MTP.rdf")
name= rdflib.term.URIRef('http://schema.org/givenName')
coord=rdflib.term.URIRef('http://www.semanticweb.org/ludo1/ontologies/2021/2/gare#coordinate')
trans=rdflib.term.URIRef('http://www.semanticweb.org/ludo1/ontologies/2021/2/gare#transport')
data=rdflib.term.URIRef('http://schema.org/data')
cord=rdflib.term.URIRef('http://schema.org/coord')
gare= dict()
for row in g.query(qres, initBindings={'z': data, 'c':name, 't':trans, 'co': cord, 'h':coord}):
    print(row)
    row = str(row)
    txt=row.split("'")

    # if(row[1] in gare.keys()){
    #     gare[row[1]]=[gare[row[1]],row[3]]
    # }