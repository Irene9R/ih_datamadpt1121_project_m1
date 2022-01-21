import pandas as pd
import numpy as np
import bs4
import requests
from shapely.geometry import Point
import geopandas as gpd
import warnings



#funtions to clean, unify, consolidate and normalize data

#funciton1
def split_lat_long_and_cleaning(df_bicimad):
    #funtion to separate latitud and longitude in two columns, to be able to make calculations for the project.
    split_df = pd.DataFrame(df_bicimad['geometry.coordinates'].to_list(), columns = ['location.longitude', 'location.latitude'])
    df_bicimad['geometry.coordinates'] = split_df['location.longitude']
    df_bicimad = df_bicimad.rename(columns={'geometry.coordinates':'location.longitude'})
    df_bicimad['location.latitude'] = split_df['location.latitude']
    #change the object type of columns "latitude" and "longitude" to float
    bicimad_df = df_bicimad.astype({'location.latitude': float, 'location.longitude': float})
    #create a new dataframe with selected columns. 
    return bicimad_df

#function2
def filtering_BiciMad_stations_by_bike_availability(df,column_name):
    bicimad_filtered_df = df[df[column_name] > 1]
    return bicimad_filtered_df

