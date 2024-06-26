import pandas as pd
import matplotlib.pyplot as plt

water_data = pd.read_csv("3.3.1_Water_Data - BKB_WaterQualityData_2020084.csv", header=0)   # identify the header row

#was used to find the rate per state
'''

#Supposed to graph a specific rate from the csv file vs time(decimal years) with ditinguishment based on site
def rate_for_each_site_vs_decimal_year(rate,y_label):
    #All distinct site value
    unique_sites = water_data["Site_Id"].unique()

    print(unique_sites)
    #Loops through all site values
    for site in unique_sites:
        #finds the data for the rate where ti has the same site id
        rate = water_data[water_data['Site_Id'] == site][rate]
       #finds the data for time where it has the same site id
        time = water_data[water_data['Site_Id'] == site]['Decimal Year']

        #plots the data with a label assigned to the specific site
        plt.plot(time,rate,label = site )
    #x axis label
    plt.xlabel("Time(Decimal Years)")
    #y_label = "Salinity(ppt): "  + site
    #y axis label(based on the parameter since this is used for numerous rates)
    plt.ylabel(y_label)

    #sused to distinguish the lines of each site by labelling which color is each line
    plt.legend()
    
     
    plt.show()
'''

    
def find_average_rate_per_year_vs_year(rate,y_label):


    #the average values for  the rate each year assigned to this list
    rate_average = []
    if(y_label != rate):
        y_label = rate

    #Finding the unique year values to find the average salinity rate and water temperature in each year
    unique_years = water_data["Year"].unique()
    print(unique_years)
    #for looping in each year to find the average
    for year in unique_years:
        # Collecting the salinity data for the specified year 
    
        #This is to stop the data analysis till that specific year
        rate_per_year = water_data[water_data['Year'] == year][rate]
        #removes all nan collumns
        rate_per_year.dropna()
        print("Rate Per Year:",rate_per_year)
        #Finding the mean of the data
        rate_mean = rate_per_year.mean()
        #adding the data to the lsit
        rate_average.append(rate_mean)

        print("Year:",year,"Salinity(ppt)",rate_mean)

    
    plt.plot(unique_years,rate_average)
    plt.xlabel("Time(Years)")
    #y_label = "Salinity(ppt): "  + site
    plt.ylabel(y_label)
    plt.legend()

    plt.show()


   
find_average_rate_per_year_vs_year('Salinity (ppt)',"Average Salinity(ppm)")
#find_average_rate_per_year_vs_year('pH (standard units)', "ph")

#salinity_rate_based_on_site("Time(Decimal Years)","Salinity Rate(ppm)")







