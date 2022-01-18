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
pd.set_option('display.width', 1000)

#Variables
url1 = "https://datos.madrid.es/egob/catalogo/202318-0-escuelas-infantiles.json"
url2 = "https://datos.madrid.es/egob/catalogo/202311-0-colegios-publicos.json"  
path = "data/dbo.bicimad_stations.csv"
path1 = "data/BiciMad_complete_version.csv"
path2 = "data/BiciMad_vs_Place_Of_Interest.csv"

if __name__ == '__main__':
    #main code
    #warnings.filterwarnings('ignore')

    #acquisition
    df1 = ac.data_adquisition_json(url1)
    df2 = ac.data_adquisition_json(url2)
    places_of_interest_df = ac.concatenate_databases(df1,df2)
    bicimad_df = ac.data_adquisition_csv(path)

    #wrangling
    bicimad_cleaned_df = wr.split_lat_long_and_cleaning(bicimad_df)

    #analysis
    an.add_key_column(places_of_interest_df)
    an.add_key_column(bicimad_cleaned_df)
    an.apply_mercator_to_df(bicimad_cleaned_df)
    an.apply_mercator_to_df(places_of_interest_df)
    merged_df = an.merging_by_column (places_of_interest_df,bicimad_cleaned_df,"key")
    total_df = an.apply_distance_to_df(merged_df)
    final_df_complete_version = an.filtering_closest_bicimad_station_to_place_of_interest(total_df)


    #reporting
    rp.save_data_to_csv(final_df_complete_version,path1)
    project1_fdf = pd.DataFrame(columns = ["Place of interest","Place address","BiciMAD station","Station location","Distance"])
    project1_fdf[["Place of interest","Place address","BiciMAD station","Station location","Distance"]] = final_df_complete_version[["title","address.street-address","name","address","distance"]]
    rp.save_data_to_csv (project1_fdf,path2)
    print (project1_fdf)