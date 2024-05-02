import pandas as pd
import matplotlib.pyplot as plt

water_data = pd.read_csv("3.3.1_Water_Data - BKB_WaterQualityData_2020084.csv", header=0)   # identify the header row

unique_sites = water_data["Site_Id"].unique()
print(unique_sites)

all_salinity = []
all_sites = []

# with grouping
for site in unique_sites:
  water_Data = water_data[water_data['Site_Id'] == site].groupby('Year')['Salinity (ppt)']
  print (site, water_Data.sum())
  all_salinity.append(water_Data.sum())
  all_sites.append(site)    

for site in all_sites:
    years = water_data.keys()
    plt.plot(years, water_Data, label=site)
    
