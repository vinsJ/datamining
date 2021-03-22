import rdflib, re
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

g.load("../MTP.rdf")
name= rdflib.term.URIRef('http://schema.org/givenName')
coord=rdflib.term.URIRef('http://www.semanticweb.org/ludo1/ontologies/2021/2/gare#coordinate')
trans=rdflib.term.URIRef('http://www.semanticweb.org/ludo1/ontologies/2021/2/gare#transport')
data=rdflib.term.URIRef('http://schema.org/data')
cord=rdflib.term.URIRef('http://schema.org/coord')

gare= dict()

for row in g.query(qres, initBindings={'z': data, 'c':name, 't':trans, 'co': cord, 'h':coord}):
    row = str(row)
    name = re.search("'(.*?)'|\"(.*?)\"", row).group(0).replace('"',"'")
    info = re.findall("'(.*?)'|\"(.*?)\"", row)
    line = info[-1][0]
    coord = info[1][0]
    if (not name in gare.keys()):
      gare[name] = {'coordinates':[coord], 'lines':line.split(',')}
    else:
        if len(gare[name]['coordinates'])<2:
            gare[name]['coordinates'].append(coord)
        else:
            gare[name]['lines'].append(line)
print(gare)