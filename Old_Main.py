import pandas as pd
import matplotlib.pyplot as plt

water_data = pd.read_csv("3.3.1_Water_Data - BKB_WaterQualityData_2020084.csv", header=0)   # identify the header row




#raw code that can be reused for later purposes

    
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
        rate_per_year.dropna()
        print("Rate Per Year:",rate_per_year)
        #Finding the mean of the data
        rate_mean = rate_per_year.mean()
        #adding the data to the lsit
        rate_average.append(rate_mean)


        '''
        # Collecting the temperature data for the specified year 
        temp_per_year = water_data[water_data['Year'] == year]['Water Temp (?C)']
        #Finding the mean of the data
        temp_mean = temp_per_year.mean()
        #adding the data to the lsit
        temp_average.append(temp_mean)


        #print("Year:",year,"Water_Temp(C)",temp_mean)
        '''
        print("Year:",year,"Salinity(ppt)",rate_mean)

    
    plt.plot(unique_years,rate_average)
    plt.xlabel("Time(Years)")
    #y_label = "Salinity(ppt): "  + site
    plt.ylabel(y_label)
    plt.legend()

    plt.show()


    '''
    plt.plot(unique_years,temp_average)
    plt.xlabel("Time(Years)")
    #y_label = "Salinity(ppt): "  + site
    plt.ylabel(" Average Temp(C*) per year")
    plt.legend()

    plt.show()
    '''
find_average_rate_per_year_vs_year('Salinity (ppt)',"Average Salinity(ppm)")
#find_average_rate_per_year_vs_year('pH (standard units)', "ph")

#salinity_rate_based_on_site("Time(Decimal Years)","Salinity Rate(ppm)")







