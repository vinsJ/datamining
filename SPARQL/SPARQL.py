import rdflib

import rdflib 
from rdflib.plugins.sparql import prepareQuery

qres = prepareQuery(
    """
    SELECT DISTINCT ?name ?coord ?trans
       WHERE {
        ?x ?z ?name .
        ?x ?y ?coord .
        ?x ?w ?trans
       }
       """)
g = rdflib.Graph()
#Nantes
#Lille
#IDF
g.load("./Nantes/Nantes.rdf")
name= rdflib.term.URIRef('http://schema.org/givenName')
coord=rdflib.term.URIRef('http://www.semanticweb.org/ludo1/ontologies/2021/2/gare#coordinate')
trans=rdflib.term.URIRef('http://www.semanticweb.org/ludo1/ontologies/2021/2/gare#transport')
gare= dict()
for row in g.query(qres, initBindings={'z': name,'y':coord, 'w':trans}):
    row = str(row)
    txt=row.split("'")
    print(txt[1],txt[3],txt[7])
    # if(row[1] in gare.keys()){
    #     gare[row[1]]=[gare[row[1]],row[3]]
    # }
print(g.query(qres, initBindings={'z': name,'y':coord}) )