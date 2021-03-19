from django.shortcuts import render, redirect
import os
import folium

# Create your views here.
def home(request):

    # folium
    # Center of France : [46.227638,2.213749]

    m = folium.Map(location=[48.866669,  2.33333],zoom_start=12)
    folium.Marker([48.8763,  2.3254], popup  = "Paris Saint Lazare", icon=folium.Icon(color='red', icon='train', prefix='fa')).add_to(m)

    ## adding to view

    ## exporting
    m=m._repr_html_()
    context = {'my_map': m}

    ## rendering
    return render(request,'geoApp/home.html',context)
