"""
Module with functions to extract JSON data to flat two dimensional table
"""

import pandas as pd
import numpy as np
import json


def clean_excel_data(df, city_name):
    """
    Function to clean the raw excel data and make it ready for
    data preparation

    Paramters:
    ----------
    The data frame to clean
    """

    # Drop the links column
    df.drop('car_links', axis=1, inplace=True)

    column_names = df.columns.to_list()
    # Convert data to JSON format
    for column_name in column_names:
        # Replace single quotes with double quotes to make the data readable by json.loads function
        df[column_name] = df[column_name].str.replace('\'', '"')
        df[column_name] = df[column_name].str.replace('None', '"None"')

    intermediate_file_path = 'C:\\Users\\PAPPILON\\Downloads\\intermediate_' + city_name + '.xlsx'
    #df.to_excel('C:\\Users\\PAPPILON\\Downloads\\intermediate_kolkata_dat.xlsx')
    df.to_excel(intermediate_file_path)

    # Add the city name as a column
    df['City'] = city_name

    return df


def new_car_detail_col_data_formatter(df):
    """
    Custom function to convert key-value dictionary data
    into column values in new_car_detail column
    """

    # Get the list of keys in the dictionary inside the cell
    # values in the new_car_detail column
    first_cell_val_dict_str = df.iloc[0]['new_car_detail'] # first cell from the specified column
    first_cell_val_dict = json.loads(first_cell_val_dict_str) # converts the string and returns a dictionary
    keys = first_cell_val_dict.keys()  # returns a list of all keys in the mentioned dictionary

    # Flatten table by going through each cell and using the keys as column names
    # and corresping values as value for the column
    # Roundabout way, but json_normalise doesnt work directly
    no_rows = len(df)
    # create columns with keys first
    for key in keys:
        df[key] = ""

    # Fill values in above created columns
    for row in range(no_rows):

        # Get the cell value as dictionary
        cell_val_dict_str = df.iloc[row]['new_car_detail']
        cell_val_dict = json.loads(cell_val_dict_str)

        # For each value corresponding to key (column), fill the value at the column
        for key in keys:
            df.at[row, key] = cell_val_dict[key]

    # Drop the new_car_detail column
    df.drop('new_car_detail', axis=1, inplace=True)

    return df


def new_car_overview_col_data_formatter(df):
    """
    Custom function to convert key-value dictionary data
    into column values in new_car_overview column
    """
    first_cell_val_dict_str = df.iloc[0]['new_car_overview']
    first_cell_val_dict = json.loads(first_cell_val_dict_str)
    top_dict_list = first_cell_val_dict['top']

    # Get the keys and create corresponding columns in dataframe
    for i in range(len(top_dict_list)):
        key = top_dict_list[i]['key']
        df[key] = ""

    no_rows = len(df)

    # Fill values in above created columns
    for row in range(no_rows):

        # Get the cell value as dictionary
        cell_val_dict_str = df.iloc[row]['new_car_overview']
        cell_val_dict_list = json.loads(cell_val_dict_str)['top']
        for i in range(len(cell_val_dict_list)):
            key = cell_val_dict_list[i]['key']
            value = cell_val_dict_list[i]['value']
            df.at[row, key] = value

    # Drop the new_car_overview column
    df.drop('new_car_overview', axis=1, inplace=True)

    return df


def new_car_feature_col_data_formatter(df):
    """
    Custom function to convert key-value dictionary data
    into column values in new_car_feature column
    """

    no_rows = len(df)

    # Fill values in the to be created columns - this is outer For loop
    for row in range(no_rows):

        cell_val_dict_str = df.iloc[row]['new_car_feature']

        # Get values in 'top' key in dictionary in cell (has list of dictionary of values)
        cell_val_dict_top_list = json.loads(cell_val_dict_str)['top']
        for i in range(len(cell_val_dict_top_list)):
            feature_col_name = cell_val_dict_top_list[i]['value']
            # If column already exists in database, add the flag value 1
            if feature_col_name in df.columns:
                df.at[row, feature_col_name] = 1
            # Else create a column and fill the entries for previous rows to zero
            else:
                df = df.copy()  # To avoid highly defragmented data frame - as suggested by pandas
                df[feature_col_name] = 0
                df.at[row, feature_col_name] = 1

        # Get the values in 'data' key in dictionary in cell
        cell_val_dict_data_list = json.loads(cell_val_dict_str)['data']
        # Since the data key has a list of dictionaries within itself, iterate for each
        # list item and extract the dictionary from them
        for i in range(len(cell_val_dict_data_list)):

            cell_val_dict_data_list_i = cell_val_dict_data_list[i]['list']

            for j in range(len(cell_val_dict_data_list_i)):
                feature_col_name = cell_val_dict_data_list_i[j]['value']
                # If column already exists in dataframe, add the flag value 1
                if feature_col_name in df.columns:
                    df.at[row, feature_col_name] = 1

                else:
                    df = df.copy()  # To avoid highly defragmented data frame - as suggested by pandas
                    # Else create a column and fill the entries for previous rows to zero
                    df[feature_col_name] = 0
                    df.at[row, feature_col_name] = 1

    # Drop the new_car_feature column
    df.drop('new_car_feature', axis=1, inplace=True)

    return df


def new_car_specs_col_data_formatter(df):
    """
    Custom function to convert key-value dictionary data
    into column values in new_car_specs column
    """
    no_rows = len(df)

    # Fill values in above created columns
    for row in range(no_rows):

        cell_val_dict_str = df.iloc[row]['new_car_specs']

        # Get values in 'top' key in dictionary in cell
        cell_val_dict_top_list = json.loads(cell_val_dict_str)['top']
        for i in range(len(cell_val_dict_top_list)):
            key = cell_val_dict_top_list[i]['key']
            value = cell_val_dict_top_list[i]['value']
            # If column already exists in the dataframe, set the value for this row, column
            if key in df.columns:
                df.at[row, key] = value
            else:
                # Else, create a new column and set the value for this row, column
                df = df.copy()  # To avoid highly defragmented data frame - as suggested by pandas
                df[key] = ""
                df.at[row, key] = value

        # Get the values in 'data' key in dictionary in cell
        cell_val_dict_data_list = json.loads(cell_val_dict_str)['data']
        # Since the data key has a list of dictionaries within itself, iterate for each
        # list item and extract the dictionary from them
        for i in range(len(cell_val_dict_data_list)):

            cell_val_dict_data_list_i = cell_val_dict_data_list[i]['list']

            for j in range(len(cell_val_dict_data_list_i)):
                specification_col_name = cell_val_dict_data_list_i[j]['key']
                specification_value = cell_val_dict_data_list_i[j]['value']
                # If column already exists in dataframe, add the flag value 1
                if specification_col_name in df.columns:
                    df.at[row, specification_col_name] = specification_value

                else:
                    df = df.copy()  # To avoid highly defragmented data frame - as suggested by pandas
                    # Else create a column and fill the entries for previous rows to zero
                    df[specification_col_name] = ""
                    df.at[row, specification_col_name] = specification_value

    # Drop the new_car_specs column
    df.drop('new_car_specs', axis=1, inplace=True)

    return df


def extract_data(df, city_name):
    """
    Wrapper function to call relevant functions to extract JSON
    in dataframe read from excel and convert it into a flat 2 dimensional dataframe

    Parameters:
    ----------
    df: DataFrame
        The data frame to extract the JSON data from
    city_name: The name of the city that corresponds to the data

    Returns:
    -------
    Extracted data as a flat table of type DataFrame object

    """
    df = clean_excel_data(df, city_name)
    df = new_car_detail_col_data_formatter(df)
    df = new_car_overview_col_data_formatter(df)
    df = new_car_feature_col_data_formatter(df)
    df = new_car_specs_col_data_formatter(df)

    return df