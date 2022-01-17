import pandas as pd
import numpy as np
import bs4
import requests
from shapely.geometry import Point
import geopandas as gpd
import warnings



#funtions to clean, unify, consolidate and normalize data

#funciton1
def split_lat_long_and_cleaning(bicimad_df):
    #funtion to separate latitud and longitude in two columns, to be able to make calculations for the project. 
    bicimad_df[['location.longitude','location.latitude']] = bicimad_df['geometry_coordinates'].str.split(',',expand=True)
    bicimad_df['location.longitude'] = bicimad_df['location.longitude'].str.replace("[","")
    bicimad_df['location.latitude'] = bicimad_df['location.latitude'].str.replace("]","")
    #change the object type of columns "latitude" and "longitude" to float
    bicimad_df = bicimad_df.astype({'location.latitude': float, 'location.longitude': float})
    #create a new dataframe with selected columns. 
    new_bicimad_df = bicimad_df.loc[:,['id','name','address','dock_bikes','free_bases','location.longitude','location.latitude']]
    return bicimad_df

