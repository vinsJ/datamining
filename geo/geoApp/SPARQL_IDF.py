import json

import rdflib
import re
from rdflib.plugins.sparql import prepareQuery

def get_IDF(path):
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

    name = rdflib.term.URIRef('http://schema.org/givenName')
    coord = rdflib.term.URIRef(
        'http://www.semanticweb.org/ludo1/ontologies/2021/2/gare#coordinate')
    trans = rdflib.term.URIRef(
        'http://www.semanticweb.org/ludo1/ontologies/2021/2/gare#transport')


    gare = dict()
    for row in g.query(qres, initBindings={'z': name, 'y': coord, 'w': trans}):
        row = str(row)
        name = re.search("'(.*?)'|\"(.*?)\"",
                        row).group(0).replace("'", "").replace('"', "")
        coord = float(re.search("'(\d+\.\d+)'", row).group(0).replace("'", ""))
        line = re.findall("'(\w+\s?\w+?)'", row)[-1]
        if (not name in gare.keys()):
            gare[name] = {'coordinates': [coord], 'lines': [line]}
        else:
            if len(gare[name]['coordinates']) < 2:
                gare[name]['coordinates'].append(coord)
            else:
                if(not line in gare[name]['lines']):
                    gare[name]['lines'].append(line)

    idf_stations = {"Location": "IDF", "Stations": gare}
    return idf_stations
