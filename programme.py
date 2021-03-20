import json
import requests
import os

jena_bin="E:/OneDrive/Documents/ESILV A4 2020-2021/Web_datamining/datamining/jena/bat"

os.chdir(jena_bin)
os.system("riot.bat --output=RDF/XML ../../datamining/Lille.jsonld> ../../datamining/Lille.rdf")





