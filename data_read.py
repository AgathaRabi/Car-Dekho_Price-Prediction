import pandas as pd
import json as js

# Read the excel files
kolkata_data = pd.read_excel("C:\\Users\\PAPPILON\\Downloads\\kolkata_cars.xlsx")
jaipur_data = pd.read_excel("C:\\Users\\PAPPILON\\Downloads\\jaipur_cars.xlsx")
delhi_data = pd.read_excel("C:\\Users\\PAPPILON\\Downloads\\delhi_cars.xlsx")
hyderabad_data = pd.read_excel("C:\\Users\\PAPPILON\\Downloads\\hyderabad_cars.xlsx")
bangalore_data =pd.read_excel("C:\\Users\\PAPPILON\\Downloads\\bangalore_cars.xlsx")
chennai_data = pd.read_excel("C:\\Users\\PAPPILON\\Downloads\\chennai_cars.xlsx")

#print(kolkata_data)



#df_new1= pd.DataFrame()
#df_new1.columns = ["Fuel Type", "Kilometers Driven"]
"""for index in range(kolkata_data.shape[0]):
    df_kolkata = js.loads(kolkata_data['new_car_detail'])"""

"""kolkata_data_test = pd.DataFrame.from_dict(kolkata_data['new_car_detail'])
kolkata_data_test = pd.DataFrame.from_dict(kolkata_data['new_car_detail'])"""

"""kolkata_data_test = kolkata_data.explode('new_car_detail', ignore_index = False)
kolkata_data_test.to_excel('C:\\Users\\PAPPILON\\Downloads\\kolkata_data_df_test150625AN.xlsx')"""

"""kolkata_data_test = pd.DataFrame(kolkata_data['new_car_detail'])
kolkata_data_test.explode(['new_car_detail'])
kolkata_data_test.to_excel('C:\\Users\\PAPPILON\\Downloads\\kolkata_data_df_test150625AN.xlsx')"""

def structured_dataframe(df):
    #get column names:
    column_names = df.columns.to_list()
    normalized_dataframe = pd.DataFrame()
    # normalize each column in dataframe and construct dataframe
    for column_name in column_names:
        normalized_column = pd.json_normalize(df[column_name])
        normalized_dataframe = pd.concat([normalized_dataframe, normalized_column], axis = 1)
    return normalized_dataframe

structured_kolkata_data = structured_dataframe(kolkata_data)
structured_kolkata_data.to_excel('C:\\Users\\PAPPILON\\Downloads\\kolkata_data_df_test150625AN.xlsx')

"""normalized_dataframe = pd.json_normalize(kolkata_data)
normalized_dataframe.to_excel('C:\\Users\\PAPPILON\\Downloads\\kolkata_data_df_test150625AN.xlsx')"""

#(pd.concat([df.drop(column_name, axis = 1), normalized_dataframe], axis = 1)))