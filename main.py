#imports
import pandas as pd
import numpy as np
import bs4
import requests
from shapely.geometry import Point
import geopandas as gpd
import warnings
from p_acquisition import acquisition as ac
from p_wrangling import wrangling as wr
from p_analysis import analysis as an
from p_reporting import reporting as rp
pd.set_option('display.max_rows', 309)
pd.set_option('display.max_columns', 7)
pd.set_option('display.width',1500)

#Variables
url1 = "https://datos.madrid.es/egob/catalogo/202318-0-escuelas-infantiles.json"
url2 = "https://datos.madrid.es/egob/catalogo/202311-0-colegios-publicos.json" 
url3 = 'https://openapi.emtmadrid.es/v1/mobilitylabs/user/login/'
url4 = 'https://openapi.emtmadrid.es/v1/transport/bicimad/stations/' 
path1 = "data/BiciMad_complete_version.csv"
path2 = "data/BiciMad_vs_Place_Of_Interest.csv"


if __name__ == '__main__':
    #main code
    warnings.filterwarnings('ignore')

    #acquisition
    df1 = ac.data_adquisition_datosmadrid_json(url1)
    df2 = ac.data_adquisition_datosmadrid_json(url2)
    places_of_interest_df = ac.concatenate_databases(df1,df2)
    bicimad_df = ac.data_adquisition_APIBiciMad_json(url3,url4)

    #wrangling
    bicimad_cleaned_df = wr.split_lat_long_and_cleaning(bicimad_df)
    bicimad_filtered_df = wr.filtering_BiciMad_stations_by_bike_availability(bicimad_cleaned_df,'dock_bikes')

    #analysis
    an.add_int_value_column (places_of_interest_df,"key",1)  #I add a "key" column in both dataframes for merging purposes
    an.add_int_value_column (bicimad_filtered_df,"key",1)
    an.apply_mercator_to_df(bicimad_filtered_df)
    an.apply_mercator_to_df(places_of_interest_df)
    merged_df = an.merging_by_column (places_of_interest_df,bicimad_filtered_df,"key")
    total_df = an.apply_distance_to_df(merged_df)
    final_df_complete_version = an.filtering_closest_bicimad_station_to_place_of_interest(total_df)
    an.direction_converter_for_google_maps(final_df_complete_version,"title","point_of_interest_google_maps")
    an.direction_converter_for_google_maps(final_df_complete_version,"name","BiciMad_google_maps")
    final_df_complete_version["url_google_maps"] = "https://www.google.com/maps/dir/"+final_df_complete_version["point_of_interest_google_maps"]+"/"+"Bicimad"+"+"+final_df_complete_version["BiciMad_google_maps"]

    #reporting
    rp.save_data_to_csv(final_df_complete_version,path1)
    project1_fdf = pd.DataFrame(columns = ["Place of interest","Place address","BiciMAD station","Station location","Distance","Available Bikes","URL google maps"])
    project1_fdf[["Place of interest","Place address","BiciMAD station","Station location","Distance","Available Bikes","URL google maps"]] = final_df_complete_version[["title","address.street-address","name","address","distance","dock_bikes","url_google_maps"]]
    rp.save_data_to_csv (project1_fdf,path2)
    print ("The information have been downloaded successfully as a csv file in your data folder. Come back soon for the lastest data on Bicimad stations availability!")