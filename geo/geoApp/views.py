from django.shortcuts import render, redirect
import folium
import os

import os
from django.conf import settings

STATIC_ROOT = os.path.join(settings.BASE_DIR, 'static/data')

import json

list_data = []

with open(f"{STATIC_ROOT}/IDF.json") as fileJ:
    data = json.load(fileJ)
    list_data.append(data)

with open(f"{STATIC_ROOT}/Lille.json") as fileJ:
    data = json.load(fileJ)
    list_data.append(data)

with open(f"{STATIC_ROOT}/Lyon.json") as fileJ:
    data = json.load(fileJ)
    list_data.append(data)

with open(f"{STATIC_ROOT}/MTP.json") as fileJ:
    data = json.load(fileJ)
    list_data.append(data)

with open(f"{STATIC_ROOT}/Nantes.json") as fileJ:
    data = json.load(fileJ)
    list_data.append(data)

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
    # Center of France : [46.227638,2.213749]

    # link of icon : https://fontawesome.com/icons?d=gallery&p=2&q=train

    m = folium.Map(location=[48.866669,  2.33333],zoom_start=6)

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