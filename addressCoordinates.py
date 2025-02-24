import pandas as pd
import numpy as np
import geopandas as gpd
from geopy.geocoders import Nominatim
import gspread
import time
import logging

# Create logging settings
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

# Setup
gc = gspread.service_account(filename='creds.json')
sh = gc.open('ContactBackup08-08-2023').sheet1
geolocator = Nominatim(user_agent="my-client-app")

df = pd.DataFrame(sh.get_all_records())
logging.debug(df.head())
logging.debug(df.columns)
df = df[df['Client?']=='TRUE']
logging.debug(df.head())




def my_geocoder(row):
    time.sleep(1.1)
    search_term = ''
    if row['Home Street']:
        search_term = str(row['Home Street'])
    if row['Home City']:
        search_term = search_term + str(row['Home City'])
    if row['Home State']:
        search_term = search_term + str(row['Home State'])
    if row['Home Postal Code']:
        search_term = search_term + str(row['Home Postal Code'])
    try:
        point = geolocator.geocode(search_term).point
        return pd.Series({'Latitude': point.latitude, 'Longitude': point.longitude})
    except:
        return pd.Series({'Latitude': None, 'Longitude': None})

df[['Latitude', 'Longitude']] = df.apply(lambda x: my_geocoder(x), axis=1)

logging.info("{}% of addresses were geocoded!".format((1 - sum(np.isnan(df["Latitude"])) / len(df)) * 100))

# Drop clients' addresses that were not successfully geocoded
df = df.loc[~np.isnan(df["Latitude"])]
df.to_csv('Client Data - df.csv', index=None)
df = gpd.GeoDataFrame(
    df, geometry=gpd.points_from_xy(df.Longitude, df.Latitude))
df.crs = {'init': 'epsg:4326'}
logging.debug(df.head())
df.to_csv('Client Data - gdf.csv',index=None)



