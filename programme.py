import json
import requests
import os

os.environ['JENA_HOME']="C:/apache-jena-3.10.0/apache-jena-3.10.0"
jena_bin="../../apache-jena-3.10.0/apache-jena-3.10.0/bat"

os.chdir(jena_bin)
os.system("riot.bat --output=RDF/XML ../../../Web_data_miniing/Project/teste.jsonld> ../../../Web_data_miniing/Project/teste.rdf ")





