import pandas as pd
import numpy as np




def drop_and_simple_extract(df):
    """
    :param : df: The data frame under analysis
    :return: First phase of cleaned data:
    : objective : To drop columns deemed not necessary, at the first phase of observation.
                  And also do data extraction from columns which don't need preprocessing of data

    """

    df['hp of vehicle'] = df['Max Power'].str.extract(r'([-+]?\d*\.?\d+)') # to rework # actually this too has unfilled rows
    #df['hp of vehicle'] = df['Max Power'].str.extract(r'(\d+.\d+)').astype('float')
    df = df.drop('it', axis=1)
    df = df.drop('trendingText', axis = 1)
    df = df.drop(['priceFixedText', 'centralVariantId'], axis=1)
    df = df.drop('Fabric Upholstery', axis=1) # drop the corollary, leather seat and fabric seat upholstery.
    #df = df.drop('Drive Modes', axis=1) # yes or no, and doesn't make sense, hence can be removed
    df = df.drop('Manually Adjustable Exterior Rear View Mirror', axis=1) # dropping the corollary for Power controlled REar view Mirror
    df = df.drop('Touch Screen Size', axis=1) # DK already specifies the presence or absence of touch screen, and this data doesn't make sense
    df = df.drop('Number Of Speaker', axis = 1) #doesn't make with the data of front and back speakers
    #df['hp of vehicle'] = df['Max Power'].str.extract(r(\d+.\d+)).astype('float')
    #df['hp of vehicle'] = df['Max Power'].str.extract(r"(\d+.\d+)")
    #df['hp of vehicle'] = df['Max Power'].str.extract('(^\d*)').astype('float')



    return df



def drop_duplicate_columns(df):

    """
        :param : df: The data frame under analysis
        :return: A further cleaned data, excluding redundant data:
        : objective : To drop columns that which are redundant.

        """

    df = df.drop('Seats', axis = 1)  # two columns of seating capacity w, HN
    df = df.drop(['owner', 'Ownership'], axis = 1) # three columns with ownership data, keeping the one with numerical value
    df = df.drop(['Kms Driven', 'transmission', 'Engine'], axis=1) # two columns with the same data for 3 parameters
    df = df.drop(['Max Torque', 'Max Power', 'Alloy Wheel Size'], axis = 1) # Max Torque has 2 cols of same data, whereas for I have extracted the needed hp.


    return df

def rename_column_names(df):

    """
    :param : df: the data frame under analysis
    :return: A further cleaned data, excluding redundant data:
    : objective : to drop columns which are redundant.

    """
    df = df.rename({'ft' : 'Fuel Type', 'bt' : 'Body Type', 'ownerNo' : 'Ownership No'}, axis = 1)
    df = df.rename({'km': 'Kilometer Driven'}, axis = 1)
    df = df.rename({'oem': 'Original Equipment Manufacturers',
                    'modelYear': 'Model Year',
                    'variantName' : 'Car Variant Details',
                    'No Of Airbags' : 'Airbags'}, axis = 1)
    df = df.rename({'Values per Cylinder': 'Valves per Cylinder',
                    'Length': 'Length of Car in mm',
                    'Width': 'Width of Car in mm',
                    'Height': 'Height of Car in mm',
                    'No Door Numbers' : 'No. of Doors',
                    'Cargo Volumn' : 'Cargo Volume in litres',
                    'Value Configuration' : 'Valve Configuration'}, axis = 1)
    df = df.rename({'price' : 'Price in Lakh'}, axis = 1)

    return df

def fill_nans(df):

    #df = df['Front Tread'].fillna(value = 0)
    #df = df['Rear Tread'].fillna(value=0)
    #df = df['Registration Year'].fillna(value = '')


    return df

def step2_clean_car_data(df):

    """
    :param : df: the data frame under analysis
    :return: second phase of cleaned data:
    : objective : extracting values only either as int or float, and discarding the units of measure and such.

    """



    df['cost_in_crore'] = df['Price in Lakh'].str.contains('Crore')
    df['cost_in_thousand'] = ~df['Price in Lakh'].str.contains('Crore|Lakh')
    df['Price in Lakh'] = df['Price in Lakh'].str.replace(",", "").str.extract(r'(\d*\.?\d+)').astype(float)
    #print(df)
    df['Price in Lakh'] = df['Price in Lakh'].where(df['cost_in_crore'] == False, other=100 * df['Price in Lakh'])
    df['Price in Lakh'] = df['Price in Lakh'].where(df['cost_in_thousand'] == False, other=df['Price in Lakh'] / 100000)
    df.drop('cost_in_crore', axis=1, inplace=True)
    df.drop('cost_in_thousand', axis = 1, inplace=True)

    return df

def step3_clean_car_data(df):

    """
    :param : df: the data frame under analysis
    :return: third phase of cleaned data:
    : objective : extracting values only either as int or float, and this function addresses data that might need a lot of pre or post - processing

    """

    #df['Price in Lakh'] = df['Price in Lakh'].apply(lambda x : x.replace('₹', '').replace('Lakh', ''))
    #df['Price in Lakh'] = df['Price in Lakh'].replace('₹', '').replace('Lakh', '')
    #df['Wheel Size'] = df['Wheel Size']. apply(lambda x: x.replace('R', ''))
    df['Wheel Size'] = df['Wheel Size'].fillna(0).astype(str) # fill NAs with 0 as str : am doing this bcs had a problem during extraction
    df['Wheel Size'] = df['Wheel Size'].str.extract(r'(\d+)').astype('int')

    # engine displacement
    #df['Engine Displacement'] = df['Engine Displacement'].replace('cc', '')
    df['Engine Displacement'] = df['Engine Displacement'].fillna(0).astype(str)
    df['Engine Displacement'] = df['Engine Displacement'].str.extract(r'(\d+)').astype('int')
    #df['Front Tread'] = df['Front Tread'].str.extract(r'(\d+)').astype('int')

    # registration year:
    #df['Registration Year'] = df['Registration Year'].apply(lambda x: pd.to_datetime(x, format="mixed"))
    #df['Registration Year'] = df['Registration Year'].replace(r'^\s*$', np.nan, regex=True)
    df['Registration Year'] = df['Registration Year'].fillna(0).astype(str)
    df['Registration Year'] = df['Registration Year'].str.extract(r'(\d+)').astype(int)
    #df = df['Registration Year'].fillna(value=0)
    #df = int(df['Registration Year'])

    return df



def step4_clean_car_data(df):


    df['Registration Year'] = df['Registration Year'].apply(lambda x : pd.to_datetime(x, format = "mixed"))
    df['Engine Displacement'] = df['Engine Displacement'].astype(int)

    return df