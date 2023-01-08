import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import geopy
from dateutil import tz
import urllib.request, json 
from datetime import datetime, timedelta

json_master = 'http://gbfs.citibikenyc.com/gbfs/gbfs.json'


from_zone = tz.tzutc()
to_zone = tz.tzlocal()

with urllib.request.urlopen(json_master) as url:
    data = json.load(url)
    update_time = datetime.utcfromtimestamp(int(str(data['last_updated']))).replace(tzinfo=from_zone).astimezone(to_zone).strftime('%Y-%m-%d %H:%M:%S') 

    
    #Extracting dictionary of dictionaries for json extracts
    dict_var = {}
    for r in data['data']['en']['feeds']:
        dict_var[r['name']] = r['url']

print(update_time)

def call_station_info(dict_var):
    with urllib.request.urlopen(dict_var['station_information']) as url:
        data = json.load(url)
        station_index = [g['station_id'] for g in data['data']['stations']]
    
        df = pd.DataFrame.from_dict(data['data']['stations'])
        df = df[['legacy_id','name','region_id','short_name','station_type','has_kiosk','capacity']]
        df['short_name'] = df['short_name'].apply(lambda x: str(x))
    return station_index, df


def call_station_status(dict_var):
    with urllib.request.urlopen(dict_var['station_status']) as url:
        data = json.load(url)
        station_index = [g['station_id'] for g in data['data']['stations']]
    
        df = pd.DataFrame.from_dict(data['data']['stations'])
        df = df[['legacy_id','last_reported','is_installed','is_renting','is_returning','num_bikes_available','num_ebikes_available','num_bikes_disabled','num_docks_available','num_docks_disabled','station_status']]
        df['lr_timestamp_loc'] = df['last_reported'].apply(lambda x: datetime.utcfromtimestamp(int(str(x))).replace(tzinfo=from_zone).astimezone(to_zone).strftime('%Y-%m-%d %H:%M:%S'))
    return station_index, df

si_2, df_2 = call_station_info(dict_var)
si, df = call_station_status(dict_var)

from pprint import pprint
print(df.head(10))