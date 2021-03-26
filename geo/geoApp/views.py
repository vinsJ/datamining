from django.shortcuts import render, redirect
import folium
import os

import os
from django.conf import settings

from geoApp.SPARQL_IDF import get_IDF
from geoApp.SPARQL_LILLE import get_lille
from geoApp.SPARQL_LYON import get_lyon
from geoApp.SPARQL_MTP import get_mtp
from geoApp.SPARQL_NANTES import get_nantes


STATIC_ROOT = os.path.join(settings.BASE_DIR, 'static/data')

import json

list_data = []

list_data.append(get_IDF(f"{STATIC_ROOT}/IDF.rdf"))
list_data.append(get_lille(f"{STATIC_ROOT}/Lille.rdf"))
list_data.append(get_lyon(f"{STATIC_ROOT}/Lyon.rdf"))
list_data.append(get_mtp(f"{STATIC_ROOT}/MTP.rdf"))
list_data.append(get_nantes(f"{STATIC_ROOT}/Nantes.rdf"))

m = folium.Map(location=[48.866669,  2.33333],zoom_start=6)

def get_emoji(lines):
    emoji = 'train'
    if("METRO" in lines[0]):
        emoji = 'subway'
    return emoji


def get_color(lines):
    color = 'red'
    if("RER" in lines[0]):
        color = 'pink'
    if("METRO" in lines[0]):
        color = 'gray'
    if("TRAIN" in lines[0]):
        color = 'green'
    return color

# Create your views here.
def home(request):

    # folium
    m = folium.Map(location=[48.866669,  2.33333],zoom_start=6)

    # link of icon : https://fontawesome.com/icons?d=gallery&p=2&q=train

    for data_obj in list_data:
        # or data_obj['Location'] == "Nantes" or data_obj['Location'] == "Lille"
        if(data_obj['Location'] == "IDF" or data_obj['Location'] == "Nantes"):
            for key, value in data_obj['Stations'].items():
                if("GL" not in value['lines']):
                    coords = [max(value['coordinates']), min(value['coordinates'])]
                    name = key
                    lines = value['lines']
                    folium.Marker(coords, tooltip=name, popup=lines, icon=folium.Icon(
                        color=get_color(lines), icon=get_emoji(lines), prefix='fa')).add_to(m)

    ## adding to view

    ## exporting
    m=m._repr_html_()
    context = {'my_map': m}

    ## rendering
    return render(request,'geoApp/home.html',context)

def test():
    print("here")
    m1 = folium.Map(location=[48.866669,  2.33333],zoom_start=6)

    for data_obj in list_data:
    # or data_obj['Location'] == "Nantes" or data_obj['Location'] == "Lille"
        if(data_obj['Location'] == "IDF"):
            for key, value in data_obj['Stations'].items():
                if("GL" not in value['lines']):
                    coords = [max(value['coordinates']), min(value['coordinates'])]
                    name = key
                    lines = value['lines']
                    folium.Marker(coords, tooltip=name, popup=lines, icon=folium.Icon(
                        color=get_color(lines), icon=get_emoji(lines), prefix='fa')).add_to(m1)

    ## adding to view

    ## exporting
    m=m1._repr_html_()
