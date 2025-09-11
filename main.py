import pandas as pd
import data_extractor
import data_cleaner as dc


# Read the excel files:

kolkata_data = pd.read_excel("C:\\Users\\PAPPILON\\Downloads\\kolkata_cars.xlsx")
jaipur_data = pd.read_excel("C:\\Users\\PAPPILON\\Downloads\\jaipur_cars.xlsx")
delhi_data = pd.read_excel("C:\\Users\\PAPPILON\\Downloads\\delhi_cars.xlsx")
hyderabad_data = pd.read_excel("C:\\Users\\PAPPILON\\Downloads\\hyderabad_cars.xlsx")
bangalore_data =pd.read_excel("C:\\Users\\PAPPILON\\Downloads\\bangalore_cars.xlsx")
chennai_data = pd.read_excel("C:\\Users\\PAPPILON\\Downloads\\chennai_cars.xlsx")



# formatting the data

kolkata_cars_df = data_extractor.extract_data(kolkata_data, 'kolkata')
jaipur_cars_df = data_extractor.extract_data(jaipur_data, 'jaipur')
delhi_cars_df = data_extractor.extract_data(delhi_data, 'delhi')
hyderabad_cars_df = data_extractor.extract_data(hyderabad_data, 'hyderabad')
bangalore_cars_df = data_extractor.extract_data(bangalore_data, 'bangalore')
chennai_cars_df = data_extractor.extract_data(chennai_data, 'chennai')


# Cleaning of the extracted and formatted data:

chennai_cars_df = dc.clean_car_data(chennai_cars_df)


# For testing how accurately data is getting extracted

kolkata_cars_df.to_excel('C:\\Users\\PAPPILON\\Downloads\\normalised_kolkata_dat.xlsx')
jaipur_cars_df.to_excel('C:\\Users\\PAPPILON\\Downloads\\normalised_jaipur_dat.xlsx')
delhi_cars_df.to_excel('C:\\Users\\PAPPILON\\Downloads\\normalised_delhi_dat.xlsx')
hyderabad_cars_df.to_excel('C:\\Users\\PAPPILON\\Downloads\\normalised_hyderabad_dat.xlsx')
bangalore_cars_df.to_excel('C:\\Users\\PAPPILON\\Downloads\\normalised_bangalore_dat.xlsx')
chennai_cars_df.to_excel('C:\\Users\\PAPPILON\\Downloads\\normalised_chennai_dat.xlsx')

# Similarly run for other cities and concatenate all together into one big dataframe

# Cleaning still be to done. Probably better to do in a data_cleaning module.