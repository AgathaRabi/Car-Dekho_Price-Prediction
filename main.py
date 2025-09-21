import pandas as pd
import data_extractor
import data_cleaner as dc


# Read the excel files:

kolkata_data = pd.read_excel("/home/agathar/Desktop/zen projects/car dheko/data/kolkata_cars.xlsx")
jaipur_data = pd.read_excel("/home/agathar/Desktop/zen projects/car dheko/data/jaipur_cars.xlsx")
delhi_data = pd.read_excel("/home/agathar/Desktop/zen projects/car dheko/data/delhi_cars.xlsx")
hyderabad_data = pd.read_excel("/home/agathar/Desktop/zen projects/car dheko/data/hyderabad_cars.xlsx")
bangalore_data =pd.read_excel("/home/agathar/Desktop/zen projects/car dheko/data/bangalore_cars.xlsx")
chennai_data = pd.read_excel("/home/agathar/Desktop/zen projects/car dheko/data/chennai_cars.xlsx")



# formatting the data

kolkata_cars_df = data_extractor.extract_data(kolkata_data, 'kolkata')
jaipur_cars_df = data_extractor.extract_data(jaipur_data, 'jaipur')
delhi_cars_df = data_extractor.extract_data(delhi_data, 'delhi')
hyderabad_cars_df = data_extractor.extract_data(hyderabad_data, 'hyderabad')
bangalore_cars_df = data_extractor.extract_data(bangalore_data, 'bangalore')
chennai_cars_df = data_extractor.extract_data(chennai_data, 'chennai')



# Cleaning of the extracted and formatted data:

chennai_cars_df = dc.clean_car_data(chennai_cars_df)
kolkata_cars_df = dc.clean_car_data(kolkata_cars_df)


# dropping duplicate columns>

chennai_cars_df = dc.drop_duplicate_columns(chennai_cars_df)






# For testing how accurately data is getting extracted

kolkata_cars_df.to_excel('/home/agathar/Desktop/zen projects/car dheko/data/normalised_kolkata_dat.xlsx')
jaipur_cars_df.to_excel('/home/agathar/Desktop/zen projects/car dheko/data/normalised_jaipur_dat.xlsx')
delhi_cars_df.to_excel('/home/agathar/Desktop/zen projects/car dheko/data/normalised_delhi_dat.xlsx')
hyderabad_cars_df.to_excel('/home/agathar/Desktop/zen projects/car dheko/data/normalised_hyderabad_dat.xlsx')
bangalore_cars_df.to_excel('/home/agathar/Desktop/zen projects/car dheko/data/normalised_bangalore_dat.xlsx')
chennai_cars_df.to_excel('/home/agathar/Desktop/zen projects/car dheko/data/normalised_chennai_dat.xlsx')

# Similarly run for other cities and concatenate all together into one big dataframe

# Cleaning still be to done. Probably better to do in a data_cleaning module.