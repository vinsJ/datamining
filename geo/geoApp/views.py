from django.shortcuts import render, redirect
import os
import folium

# Create your views here.
def home(request):
    shp_dir = os.path.join(os.getcwd(),'media','shp')

    # folium
    m = folium.Map(location=[46.227638,2.213749],zoom_start=6)

    ## style
    style_basin = {'fillColor': '#228B22', 'color': '#228B22'}
    style_rivers = { 'color': 'blue'}

    ## adding to view
    folium.GeoJson(os.path.join(shp_dir,'basin.geojson'),name='basin',style_function=lambda x:style_basin).add_to(m)
    folium.GeoJson(os.path.join(shp_dir,'rivers.geojson'),name='rivers',style_function=lambda x:style_rivers).add_to(m)
    folium.LayerControl().add_to(m)

    ## exporting
    m=m._repr_html_()
    context = {'my_map': m}

    ## rendering
    return render(request,'geoApp/home.html',context)
