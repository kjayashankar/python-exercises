import numpy as np
import pandas
import folium

df = pandas.read_csv('Volcanoes-USA.txt')
dflat = df['LAT']
dflon = df['LON']
centerlat = dflat.mean()
centerlon = dflon.mean()

dfelev = df['ELEV']
minelev = dfelev.min()
maxelev = dfelev.max()
stepelev = (maxelev - minelev)/3

def getcolor(elev):
    if elev >= minelev and elev < stepelev:
        return 'green'
    elif elev >= stepelev and elev < 2*stepelev:
        return 'orange'
    else:
        return 'red'
map = folium.Map(location = [0,0],zoom_start=1.5)
for lat,lon,name,elev in zip(dflat,dflon,df['NAME'],dfelev):
    icon = folium.Icon(color=getcolor(elev), icon="ok")
    map.add_child(folium.Marker(location=[lat,lon],popup=name,icon=icon))

map.add_child(folium.GeoJson(data=open('geojson.json'),
name='Population',
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] <= 10000000
                                              else 'orange' if 10000000 < x['properties']['POP2005'] <= 20000000
                                              else 'red'}))

map.save('map_with_border.html')
