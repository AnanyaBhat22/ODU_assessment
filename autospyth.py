
import pandas as pd
import matplotlib.pyplot as plt # This is used for plotting the graph

#Converting a csv file into data-frame (csv file name is taken as input)
data=pd.read_csv('autos.csv',encoding='latin-1')

#To find the average of the price
avg=data.price.mean()
print('Average price is : ',avg)

#To list the different possible vehicle types
dif_vehi_type=data.vehicleType.unique()     #unique lists all the unique(non-repeatative values)
print('List of different possible vehicle types : ',dif_vehi_type)

#To give the lowest and the highest year of registration respsectively
lowRegYear=data.yearOfRegistration.min()
highRegYear=data.yearOfRegistration.max()
print('lowest year of registration is : ',lowRegYear)
print('highest year of registration is : ',highRegYear)


# miny = data['yearOfRegistration'].idxmin()
# miky=data.loc[miny,'yearOfRegistration']
# print(miky)


#To find the standard deviation of the column kilometer
std_dev=data.kilometer.std()
print('standard deviation of column kilometer is : ',std_dev)

#To plot a bar graph
brandCounts = data.brand.value_counts()
brandCounts.plot(kind='bar')
plt.show()                              #to display the graph

#To find the vehicle type of the vehicle with the minimum and maximum price in the DataFrame.
min_vehicle_type = data.loc[data['price'].idxmin()]['vehicleType']    #idxmin:returns the index of the row which is min
max_vehicle_type = data.loc[data['price'].idxmax()]['vehicleType']    #loc:returns the row with min price
print('Vehicle type with minimum price:', min_vehicle_type)
print('Vehicle type with maximum price:', max_vehicle_type)

#To plot a pie chart
gearbox_counts = data['gearbox'].value_counts()
gearbox_counts.plot(kind='pie')
plt.show()
