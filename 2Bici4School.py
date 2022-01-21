#imports
import pandas as pd
import numpy as np
import bs4
import requests
from shapely.geometry import Point
import geopandas as gpd
import webbrowser
import warnings
import argparse

pd.set_option('display.max_rows', 309)
pd.set_option('display.max_columns', 7)
pd.set_option('display.width',1500)

from p_acquisition import acquisition as ac
from p_wrangling import wrangling as wr
from p_analysis import analysis as an
from p_reporting import reporting as rp

#Variables
path1 = "data/BiciMad_complete_version.csv"
path2 = "data/BiciMad_vs_Place_Of_Interest.csv"

# Argument parser function
def argument_parser():
    parser = argparse.ArgumentParser (description="Welcome to 2Bici4School!!! This program will return the closest bicimad station with available bikes to <all> or <an specific> Preschool or Public School in Madrid.\nImportant information: BiciMad bicicles can be used from the age of 14. \n Minors under 16 must be registered by an adult, acting as a guardian or legal representative, and will assume full responsibility for both the acts of minors while using the service and their physical suitability to use the service.\n The helmet is mandatory for those under 16 years of age.\n By the way congratulations on your english kid!!")
    #parser.add_argument("-g", "--group_by_category", choices = ["Escuelas infantiles - Preschool","Colegios Públicos - Public Schools"], help ="returns the Bicimad stations nearest to an specific group of places of interest)
    parser.add_argument("-l", "--list", action = "store_true", help ="displays a list of all places of interest available in the data.")
    parser.add_argument("-s", "--single_option", action="store_true", help = "displays the nearest BiciMad station with availability to a single place of interest.")
    parser.add_argument("-a", "--all", action = "store_true", help = "displays a list of all <places of interes> and their nearest BiciMad station with available bikes.")
    parser.add_argument("-i", "--information_BiciMad", action = "store_true", help ="displays the <frequent questions> page of BiciMad.")
    parser.add_argument("-m", "--BiciMad_stations_map", action = "store_true", help ="displays a map of all Bicimad stations.")
    args = parser.parse_args()
    return args


#Main pipeline function:                 

def main(arguments):
    if arguments.list:
        imported_final_complete_version_df = ac.data_adquisition_csv(path1)
        print("The list of the <places of interest> in data is: ")
        print(imported_final_complete_version_df["title"])
    elif arguments.all:
        project1_fdf = ac.data_adquisition_csv(path2)
        user_visual_df = pd.DataFrame(columns = ["Place of interest","Place address","BiciMAD station","Station location","Available Bikes"])
        user_visual_df[["Place of interest","Place address","BiciMAD station","Station location","Available Bikes"]] = project1_fdf[["Place of interest","Place address","BiciMAD station","Station location","Available Bikes"]]
        print (user_visual_df)
    elif arguments.single_option:
        project1_fdf = ac.data_adquisition_csv(path2)
        user_visual_df = pd.DataFrame(columns = ["Place of interest","Place address","BiciMAD station","Station location","Available Bikes"])
        user_visual_df[["Place of interest","Place address","BiciMAD station","Station location","Available Bikes"]] = project1_fdf[["Place of interest","Place address","BiciMAD station","Station location","Available Bikes"]]
        place_of_interest = str(input("Please enter the education center from which you would like to calculate the closest Bicimad station: "))
        print ("The closest Bicimad station to", place_of_interest,"is: ")
        print (user_visual_df.loc[user_visual_df['Place of interest'] ==place_of_interest])
        webbrowser.open(project1_fdf[project1_fdf['Place of interest'] ==place_of_interest]['URL google maps'].values[0],new=2)
    elif arguments.information_BiciMad:
        webbrowser.open("https://www.bicimad.com/index.php?s=preguntas", new=2)
    elif arguments.BiciMad_stations_map:
        webbrowser.open("https://mynavega.emtmadrid.es/MapViewer/?state={%22visibleLayers%22%3A{%22Movilidad_8158%22%3A[]}%2C%22center%22%3A%22-412623%2C4926545%2C102100%22%2C%22level%22%3A6}",new=2)  
    else:
        print ("incorrect command, review help command -h")  

if __name__ == '__main__':
    arguments = argument_parser()
    main(arguments)