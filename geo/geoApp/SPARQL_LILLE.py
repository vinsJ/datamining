import json
import rdflib , re
from rdflib.plugins.sparql import prepareQuery

def get_lille(path):
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


  g.load(path)
  name= rdflib.term.URIRef('http://schema.org/givenName')
  coord=rdflib.term.URIRef('http://www.semanticweb.org/ludo1/ontologies/2021/2/gare#coordinate')
  trans=rdflib.term.URIRef('http://www.semanticweb.org/ludo1/ontologies/2021/2/gare#transport')
  gare= dict()
  for row in g.query(qres, initBindings={'z': name,'y':coord, 'w':trans}):
      row = str(row)
      name = re.search("'(.*?)'|\"(.*?)\"", row).group(0).replace("'","").replace('"',"")
      info = re.findall("'(.*?)'|\"(.*?)\"", row)
      line = info[-1][0]
      coord = float(info[1][0])
      if (not name in gare.keys()):
        gare[name] = {'coordinates':[coord], 'lines':line.split(',')}
      else:
        if len(gare[name]['coordinates'])<2:
          gare[name]['coordinates'].append(coord)


  lille_stations = {"Location": "Lille", "Stations": gare}
  return lille_stations
