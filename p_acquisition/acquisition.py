#imports
import pandas as pd
import numpy as np
import bs4
import requests
from shapely.geometry import Point
import geopandas as gpd
import warnings

#Variables
url1 = "https://datos.madrid.es/egob/catalogo/202318-0-escuelas-infantiles.json"
url2 = "https://datos.madrid.es/egob/catalogo/202311-0-colegios-publicos.json" 
url3 = "https://openapi.emtmadrid.es/v1/mobilitylabs/user/login/"
url4 = "https://openapi.emtmadrid.es/v1/transport/bicimad/stations/"

#functions to acquire data

#functon1
def data_adquisition_datosmadrid_json(url):
    #function to connect to "Portal de datos abiertos del Ayuntamiento de Madrid", where we will have access to different "Places of Interest" datasets stored as json files. The function will connect to the API, read the dataset and transform it into a pandas dataframe.
    response_df = requests.get(url).json()
    #since the data is stored in a json, I searched the keys of the first dictionary in which the data is store, so I can collect the information I need to extract for the project. 
    response_df.keys()
    places_of_interest_df = pd.json_normalize(response_df["@graph"])
    return places_of_interest_df

#function2
def concatenate_databases(df1,df2):
    #function to concatenate the different "places of interest" databases
    conca_df = pd.concat([df1, df2])
    concatenated_df = conca_df.loc[:,['id','title','address.locality','address.postal-code','address.street-address','location.latitude','location.longitude']]
    return concatenated_df

#function3
def data_adquisition_csv(path):
    #function to retrieve the information from a csv file stored locally.  
    imported_df = pd.read_csv(path)
    return imported_df

#funtion4
def data_adquisition_APIBiciMad_json(url1,url2):
    header={'email':'irene9ago85@hotmail.com','password':'Pepper24Merlot.-'}
    get_token=requests.get(url1, headers=header).json()
    accessToken=get_token['data'][0]['accessToken']
    header = {'accessToken':str(accessToken)}
    my_dataset=requests.get(url2, headers = header).json()
    bicimad_original_df = pd.json_normalize(my_dataset['data'])
    df_bicimad = bicimad_original_df.loc[:,['id','name','address','dock_bikes','free_bases','geometry.coordinates']]
    return df_bicimad