import pandas as pd
import numpy as np
from geopy import distance as distance
from geopy.geocoders import Nominatim
import datetime as dt
from datetime import datetime

print('DAMN DUDE')

path = '/input/202210-citibike-tripdata.csv'

df = pd.read_csv(path, dtype={"end_station_id":"str","start_station_id":"str"})
df_1 = df
#Know what you're deleting
print(len(df['start_station_id'][df['start_station_id'].str.contains("SYS")==True]))
print(len(df['start_station_id'][df['start_station_id'].str.contains("Lab")==True]))
print(len(df['start_station_id'][df['start_station_id'].str.contains("JC")==True]))
print(len(df['start_station_id'][df['start_station_id'].str.contains("HB")==True]))
print(len(df['end_station_id'][df['end_station_id'].str.contains("SYS")==True]))
print(len(df['end_station_id'][df['end_station_id'].str.contains("Lab")==True]))
print(len(df['end_station_id'][df['end_station_id'].str.contains("JC")==True]))
print(len(df['end_station_id'][df['end_station_id'].str.contains("HB")==True]))

dtypess={"ride_id": "str", "rideable_type": "str","started_at":"str"
,"ended_at":"str","start_station_name":"str","start_station_id":"str"
,"end_station_name":"str","end_station_id":"str","start_lat":"float"
,"start_lng":"float","end_lat":"float","end_lng":"float","member_casual":"str"}

#Removing Aforementioned Rows
df = df[df['start_station_id'].str.contains("SYS")==False]
df = df[df['start_station_id'].str.contains("Lab")==False]
df = df[df['start_station_id'].str.contains("JC")==False]
df = df[df['start_station_id'].str.contains("HB")==False]
df = df[df['end_station_id'].str.contains("HB")==False]
df = df[df['end_station_id'].str.contains("SYS")==False]
df = df[df['end_station_id'].str.contains("Lab")==False]
df = df[df['end_station_id'].str.contains("JC")==False]

#string coerce:
#df['start_station_id']=df['start_station_id'].apply(lambda x: x.str.extract('(\d+)'))
#df['start_station_id'] = pd.to_numeric(df['start_station_id'],errors='coerce')
#df['end_station_id'] = pd.to_numeric(df['end_station_id'],errors='coerce')

#reassigning datatypes, printing the column in the loop in the event of errors
for key, value in dtypess.items():
    print(key)
    df[key] =  df[key].astype(value)


def geopy_address_query_start(x):
    geolocator = Nominatim(user_agent="geoapiExercises")
    zips = []
    addresses = []
    for i in range(len(x['start_lat'])):
        coord_1 = (x.iloc[i,1],x.iloc[i,2])
        str_res = geolocator.reverse(coord_1)
        try:
            str_zip = str_res.raw['address']['postcode']
        except:
            str_zip = '00000'
        try:
            str_add = str_res.raw['address']['suburb']
        except:
            str_add = 'No Map'

        zips.append(str_zip)
        #print(str_res.raw['address'])
        addresses.append(str_add)
    return addresses,zips

u_df_st.iloc[i,2]

#Creating Dictionary
u_df_st = df.drop_duplicates(subset=['start_station_id']).dropna()
u_df_st = u_df_st[['start_station_id','start_lat','start_lng']].dropna()
u_df_en = df.drop_duplicates(subset=['end_station_id']).dropna()
u_df_en = u_df_en[['start_station_id','start_lat','start_lng']].dropna()
u_df_st['borough'], u_df_st['zip'] = geopy_address_query_start(u_df_st)
#if ending location is not in the starting set, we add it to the first df
#unique_stations_end = u_df_en['start_station_id'].unique().tolist()
#unique_stations_end = df['end_station_id'].unique().tolist()
#unique_stations_end_cl = [x for x in unique_stations_end if str(x) != 'nan']
#unique_stations_end_1 = [x for x in unique_stations_end_cl if x not in unique_stations]

u_df_st.head(20)

u_df_st['zip'].value_counts()

print(u_df_st[u_df_st['zip'] == '00000'])
#manual intervention:
u_df_st.loc[508,'zip'] = '10019'
u_df_st.loc[2124,'zip'] = '10003'
u_df_st.loc[3372,'zip'] = '10022'
u_df_st.loc[21461,'zip'] = '10035'

lst = [508,2124,3372,21461]
u_df_st.loc[lst]


u_df_st.to_csv('/output/station_borough_zip.csv')
u_df_st_m = u_df_st[u_df_st['borough'] == 'Manhattan']
u_df_st_m.to_csv('/output/station_manhattan_zip.csv')


target = pd.DataFrame(0,index = u_df_st['start_station_id'], columns = u_df_st['start_station_id'])
print(target.shape)
target.head(20)

# import time
# start = time.time()

# for i in range(len(u_df_st['start_station_id'])):
    # for j in range(len(u_df_st['start_station_id'])):
        # if i == j:
            # target.iloc[i,j] = 0.0
        # elif target.iloc[j,i] > 0:
            # target.iloc[i,j] = target.iloc[j,i]
        # else:
            # coord_1 = (u_df_st.iloc[i,1],u_df_st.iloc[i,2])
            # coord_2 = (u_df_st.iloc[j,1],u_df_st.iloc[j,2])
            # target.iloc[i,j] = distance.distance(coord_1,coord_2).miles

# end = time.time()
# print(end-start)
