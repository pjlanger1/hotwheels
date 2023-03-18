
import requests
import json

link_to_ping = 'https://layer.bicyclesharing.net/map/v1/nyc/stations'
a = requests.get(link_to_ping).json()
dest = {}
for g in a['features']:
    dest[g['properties']['terminal']] = g['properties']

dest_json = json.dumps(dest)    