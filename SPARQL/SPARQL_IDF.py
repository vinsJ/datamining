import rdflib 
import re
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


g.load("../IDF.rdf")
name= rdflib.term.URIRef('http://schema.org/givenName')
coord=rdflib.term.URIRef('http://www.semanticweb.org/ludo1/ontologies/2021/2/gare#coordinate')
trans=rdflib.term.URIRef('http://www.semanticweb.org/ludo1/ontologies/2021/2/gare#transport')
gare= dict()
for row in g.query(qres, initBindings={'z': name,'y':coord, 'w':trans}):
    row = str(row)
    name = re.search("'(.*?)'|\"(.*?)\"", row).group(0).replace("'","").replace('"',"")
    coord = re.search("'(\d+\.\d+)'", row).group(0).replace("'","")
    line = re.findall("'(\w+\s?\w+?)'", row)[-1]
    if (not name in gare.keys()):
      gare[name] = {'coordinates':[coord], 'lines':[line]}
    else:
      if len(gare[name]['coordinates'])<2:
        gare[name]['coordinates'].append(coord)
        gare[name]['lines'].append(line)
      else:
        gare[name]['lines'].append(line)
print(gare['GARE DE LYON'])