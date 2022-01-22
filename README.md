<p align="left"><img src="https://cdn-images-1.medium.com/max/184/1*2GDcaeYIx_bQAZLxWM4PsQ@2x.png"></p>

# __2Bici4School__ #
Irene Rengifo - Project Module 1 - Data Analytics Part-Time Bootcamp - Nov 2021 - Ironhack Madrid
## **Goal** ##
The goal of **2Bici4School** is to help you find allocate the **closest BiciMad station** with **available bikes** to **preschools or public schools** in Madrid. 

## **Overview** ##
Let's imagine you're over 14 years old and near a preeschool or public school in Madrid, whether a student or just passing by the area, you decide you want to use a BiciMad, you have Google Maps, but the closest station might not always have available bikes and you just don´t want to get there to find out there is no availability. 

![Image](https://c.tenor.com/eAt5EfLNIuEAAAAC/joaquin-phoenix-commodus.gif)

**2Bici4School** will receive the name of the preschool or public school and based on that information provides you the *name*, *address*, *number of bikes available* and *directions* to the closest BiciMad station with bike availability.  It will even provide you a list of the closets BiciMad Stations to all preschools and public schools if you wish.

### **make sure you go where the bikes are!!.** ### 


![Image](https://www.vmcdn.ca/f/files/shared/miscellaneous-stock-images/kid-thumbs-up-excited.jpeg;w=960)

## **Data** ##
1. [API REST EMTMADRID-MobilityLabs](https://apidocs.emtmadrid.es/#api-Block_4_TRANSPORT_BICIMAD-List_of_Bicimad_Stations)
This API is used to get the datasets of the BiciMad stations, including location and available bikes directly, so data is real-time accurate. The EMTMADRID-MobilityLabs API requieres a username, password and accessToken to connect.

2. [API REST from Portal de datos abiertos del Ayuntamiento de Madrid](https://datos.madrid.es/nuevoMadrid/swagger-ui-master-2.2.10/dist/index.html?url=/egobfiles/api.datos.madrid.es.json#/)
This API is used to get the datasets of the Public Schools and Preschools in Madrid.  

## **Project Main Stack**

- [Azure SQL Database](https://portal.azure.com/) - used during the starting process of working on the project. 
- [Azure Data Studio](https://docs.microsoft.com/es-es/sql/azure-data-studio/?view=sql-server-ver15)  - used during the starting process of working on the project.
- [Requests](https://requests.readthedocs.io/)
- [Pandas](https://pandas.pydata.org/pandas-docs/stable/reference/index.html)
- Module `geo_calculations.py
- [Time](https://docs.python.org/3/library/time.html)
- [warnings](https://docs.python.org/3/library/warnings.html)
- [webbrowser](https://docs.python.org/es/3/library/webbrowser.html)
- [Argparse](https://docs.python.org/3.7/library/argparse.html)

## **Methodology** #
1. **Connecting to the API REST of Portal de datos abiertos del Ayuntamiento de Madrid** to get the datasets with the *name, address, latitude and longitude* of every **Preeschool and Public School** in Madrid.  


2. **Connecting to the API REST EMTMADRID-MobilityLabs** to get the dataset with the information of the **BiciMad stations**, including *name, address, latitude, longitude and bike availability*.

3. **Data in analysed** in *main.py*. We first filter the "BiciMad" information by available bikes, so we can avoid stations with no availability. Then, using the **Latitude** and **Longitude**, we calculate the mercator and distance between all **public schools/ preschools** and all **Bicimad Stations**. After having all possible combinations, we then group **public schools/ preschools** by **minimun distance** obtaining the **closest BiciMad station with availability** to each **education center**. This information is exported into the csv file: *data/BiciMad_complete_version.csv*.


4. **Improvements:** To provide a faster interface for the user of **2Bici4Schools** by avoiding for the calculations to be performed everytime the user wants to interact with the app, we import the csv generated by running *main.py* to our app and display the information the user desires. 

5. **User Options**: On **2Bici4School** the user can select between different options:

>"-l", "--list",                - *displays a list of **all places of interest available** in the data.*  
 "-s", "--single_option",       - *displays the **nearest BiciMad station with availability to a single place of interest.***  
 "-a", "--all",                 - *displays a list of all **places of interes** and their **nearest BiciMad station with available bikes.***  
"-i", "--information_BiciMad", - *displays the frequent questions page of BiciMad.*  
 "-m", "--BiciMad_stations_map" - *displays a map of all Bicimad stations.*

6. **Application Reporting:** The BiciMad will return either: 
- (-a) displaying a list in the terminal and a csv file to the user with the information of all, allocated in 
*data/BiciMad_vs_Place_Of_Interest.csv*
- (-s) displaying the information of the closest Bicimad Station in the terminal and openining a web browser tab with the directions from the selected **Preschool or Public School** to the given station, using *Google Maps*.

## **Things I'm proud of** ##
**2Bici4School** was structured in a way that it would work with any given dataset of *Places of Interest* extracted from the API REST - Portal de datos abiertos del Ayuntamiento de Madrid.

![Image](https://c.tenor.com/RPqKgAiHcQMAAAAC/self-five-barney.gif)

## **Future improvements** #
- Add several more datasets of the [API REST from Portal de datos abiertos del Ayuntamiento de Madrid] into the project.
- Add more useful information about the "place of interest" to display to the user. 

## GO GET YOUR BIKE AND HAVE A GOOD RIDE!!!
![Image](https://i.makeagif.com/media/1-26-2015/VoK2OW.gif)

