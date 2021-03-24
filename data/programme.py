import json
import requests
import os

PATH_JENA = "E:/OneDrive/Documents/ESILV A4 2020-2021/Web_datamining/datamining/jena/bat"

jena_bin = PATH_JENA

os.chdir(jena_bin)
os.system("riot.bat --output=RDF/XML ../../datamining/IDF.jsonld> ../../datamining/IDF.rdf")





