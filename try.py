import pandas as pd
import json

# Read the excel files
"""kolkata_data = pd.read_excel("C:\\Users\\PAPPILON\\Downloads\\kolkata_cars.xlsx")
jaipur_data = pd.read_excel("C:\\Users\\PAPPILON\\Downloads\\jaipur_cars.xlsx")
delhi_data = pd.read_excel("C:\\Users\\PAPPILON\\Downloads\\delhi_cars.xlsx")
hyderabad_data = pd.read_excel("C:\\Users\\PAPPILON\\Downloads\\hyderabad_cars.xlsx")
bangalore_data =pd.read_excel("C:\\Users\\PAPPILON\\Downloads\\bangalore_cars.xlsx")
chennai_data = pd.read_excel("C:\\Users\\PAPPILON\\Downloads\\chennai_cars.xlsx")


# general clean

# Drop the links column
kolkata_data.drop('car_links', axis=1, inplace=True)

column_names = kolkata_data.columns.to_list()
normalised_df = pd.DataFrame()
# Convert data to JSON format
for column_name in column_names:
    # Replace single quotes with double quotes to make the data readable by json.loads function
    kolkata_data[column_name] = kolkata_data[column_name].str.replace('\'', '"')
    kolkata_data[column_name] = kolkata_data[column_name].str.replace('None', '"None"')
kolkata_data.to_excel('C:\\Users\\PAPPILON\\Downloads\\kolkata_data_general_clean.xlsx')"""







df = {"heading": "Car overview", "top": [{"key": "Registration Year", "value": "2014", "icon": "https://images10.gaadi.com/listing/vdp/co/v1/registrationYear.svg"}, {"key": "Insurance Validity", "value": "Third Party insurance", "icon": "https://images10.gaadi.com/listing/vdp/co/v1/insuranceValidity.svg"}, {"key": "Fuel Type", "value": "Petrol", "icon": "https://images10.gaadi.com/listing/vdp/co/v1/fuel.svg"}, {"key": "Seats", "value": "5 Seats", "icon": "https://images10.gaadi.com/listing/vdp/co/v1/seats.svg"}, {"key": "Kms Driven", "value": "70,000 Kms", "icon": "https://images10.gaadi.com/listing/vdp/co/v1/kmsDriven.svg"}, {"key": "RTO", "value": "WB02", "icon": "https://images10.gaadi.com/listing/vdp/co/v1/rto.svg"}, {"key": "Ownership", "value": "Third Owner", "icon": "https://images10.gaadi.com/listing/vdp/co/v1/ownership.svg"}, {"key": "Engine Displacement", "value": "2494 cc", "icon": "https://images10.gaadi.com/listing/vdp/co/v1/engineDisplacement.svg"}, {"key": "Transmission", "value": "Automatic", "icon": "https://images10.gaadi.com/listing/vdp/co/v1/transmission.svg"}, {"key": "Year of Manufacture", "value": 2014, "icon": "https://images10.gaadi.com/listing/vdp/co/v1/yearManufacture.svg"}], "bottomData": "None"}
#cell_val_dict_list = json.loads(df)['top']

print((df)['top'])






"""for i in range(len(cell_val_dict_list)):
    key = cell_val_dict_list[i]['key']
    value = cell_val_dict_list[i]['value']
    df.at[0, key] = value
    print(value)"""