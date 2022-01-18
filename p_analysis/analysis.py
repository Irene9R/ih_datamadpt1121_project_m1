import pandas as pd
import numpy as np
import bs4
import requests
from shapely.geometry import Point
import geopandas as gpd
import warnings
for p_acquisition import acquisition as ac


#funtions

#fuction1
#Since my dataframes have no columns in common, I opted to create a new column with assign value 1 in both dataframes to merge both dataframes on this column. 
def add_key_column (df):
    #function generates a new column "key" with all row values equal 1.
    df['key'] = int(1)
    return df['key']

#function2
def to_mercator(lat, long):
    # transform latitude/longitude data in degrees to pseudo-mercator coordinates in metres
    c = gpd.GeoSeries([Point(lat, long)], crs=4326)
    c = c.to_crs(3857)
    return c

#function3
def apply_mercator_to_df(df):
    #creates a new column in a pandas dataframe by applying to_mercator function to all rows of a given pandas dataframe that has latitude and longitude data columns.
    df['mercator'] = df.apply(lambda df: to_mercator(df['location.latitude'],df['location.longitude']), axis = 1)
    return df['mercator']

#function4
def merging_by_column (df_1, df_2,column_name):
    #merges two dataframes on a selected "column name"
    merged_df = pd.merge(df_1,df_2, on=column_name, how="outer")
    return merged_df

#function5
def distance_meters(start,finish):
    # return the distance in metres between to two points
    return start.distance(finish)

#function6
def apply_distance_to_df(df):
    #creates a new column in a pandas dataframe by applying distance_meters function to all rows of a given pandas dataframe that has both mercator parameters calculated. It returns the distance in meters between two points for each row in the dataframe. 
    df['distance'] = df.apply(lambda df: distance_meters(df['mercator_x'],df['mercator_y']), axis = 1)
    total_sorted_df = df.sort_values(["title", "distance"], ascending = (True, True))
    reindex_total_sorted_df = total_sorted_df.reset_index(drop=True)
    return reindex_total_sorted_df

#function7
def filtering_closest_bicimad_station_to_place_of_interest(df):
    groupby_df = df.groupby(["title"])["distance"].min()
    total_groupby_df = pd.DataFrame(groupby_df)
    total_groupby_df_windex = total_groupby_df.reset_index(drop = False)
    final_complete_df = total_groupby_df_windex.merge(df,how="left")
    return final_complete_df