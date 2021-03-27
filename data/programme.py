import json
import requests
import os

from dotenv import load_dotenv

load_dotenv()

PATH_JENA = os.getenv('PATH_JENA')

os.chdir(PATH_JENA)
os.system("riot.bat --output=RDF/XML ../../datamining/IDF.jsonld> ../../datamining/IDF.rdf")





