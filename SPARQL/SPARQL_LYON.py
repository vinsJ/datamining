import rdflib, re
from rdflib.plugins.sparql import prepareQuery

qres = prepareQuery(
    """
    SELECT DISTINCT ?name ?trans ?coord
       WHERE {
        ?x ?z ?name .
        ?x ?y ?trans .
        ?t ?p ?x .
        ?t ?u ?coord
       }
       """)
g = rdflib.Graph()

g.load("../Lyon.rdf")
name= rdflib.term.URIRef('http://schema.org/givenName')
coord=rdflib.term.URIRef('http://www.semanticweb.org/ludo1/ontologies/2021/2/gare#coordinate')
trans=rdflib.term.URIRef('http://www.semanticweb.org/ludo1/ontologies/2021/2/gare#transport')
pers=rdflib.term.URIRef('http://www.semanticweb.org/ludo1/ontologies/2021/2/gare/45475')
prop=rdflib.term.URIRef('http://schema.org/properties')
gare= dict()
for row in g.query(qres, initBindings={'z': name,'y':trans,'p':prop,'u':coord }):
    row = str(row)
    info = re.findall("'(.*?)'|\"(.*?)\"", row)
    name = re.search("'(.*?)'|\"(.*?)\"", row).group(0).replace("'","").replace('"',"")
    line = info[1][0]
    coord = float(info[2][0])
    if (not name in gare.keys()):
      gare[name] = {'coordinates':[coord], 'lines':line.split(',')}
    else:
      if len(gare[name]['coordinates'])<2:
        gare[name]['coordinates'].append(coord)
print(gare)