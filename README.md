# Datamining final project - ESILV M1 Data&IA

Transport map using JSONLD to get information from multiples API. 

SPARQL to querry our RDF files in DJANGO when loading the page 

***Only IDF and Nantes are loaded because the map cannot handle more***

# How to run ? 

## Virtual environment

Please, install pipenv : 

-  `pip install pipenv`
- `pipenv install`
- `pipenv shell`

***Make sure to have Python 3.7 on your system, otherwise the virtual env. won't build. If you don't have it, you can change the version of python in the Pipfile (`[requires]
python_version = "3.X"`) and Pipfile.lock (in meta)***

### Remove virtual environment

Once you've test our app, you can delete the virtual env by executing :

`pipenv --rm` in the terminal.

## Django APP

When all the dependencies have been installed, you can : 

- cd in geo repository
- `python manage.py runserver`

## JsonLD to RDF

If you want to transform the data we get with the APIs, you can run data > programme.py

Please, **modify the .env file** with the path to your JENA. 

---

By Ludovic CHEVALLIER, Quentin BOURGUE and Vincent DEBANDE