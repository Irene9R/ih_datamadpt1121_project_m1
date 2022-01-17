import pandas as pd
import numpy as np
import bs4
import requests
from shapely.geometry import Point
import geopandas as gpd
import warnings


#functions

#function1
def save_data_to_csv (df,path):
    df.to_csv(path, index = False)