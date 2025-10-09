import pandas as pd


def step1_clean_car_data(df):


    df['hp of vehicle'] = df['Max Power'].str.extract(r'([-+]?\d*\.?\d+)')
    #df['hp of vehicle'] = df['Max Power'].str.extract(r'(\d+.\d+)').astype('float')
    df = df.drop('it', axis=1)
    df = df.drop('trendingText', axis = 1)
    df = df.drop(['priceFixedText', 'centralVariantId'], axis=1)
    df = df.drop('Fabric Upholstery', axis=1) # drop the corollary, leather seat and fabric seat upholstery.
    #df = df.drop('Drive Modes', axis=1) # yes or no, and doesn't make sense, hence can be removed
    df = df.drop('Manually Adjustable Exterior Rear View Mirror', axis=1) # dropping the corollary for Power controlled REar view Mirror
    df = df.drop('Touch Screen Size', axis=1) # DK already specifies the presence or absence of touch screen, and this data doesn't make sense
    df = df.drop('Number Of Speaker', axis = 1) #doesnt make with the data of front and back speakers
    #df['hp of vehicle'] = df['Max Power'].str.extract(r(\d+.\d+)).astype('float')
    #df['hp of vehicle'] = df['Max Power'].str.extract(r"(\d+.\d+)")
    #df['hp of vehicle'] = df['Max Power'].str.extract('(^\d*)').astype('float')



    return df



def drop_duplicate_columns(df):

    df = df.drop('Seats', axis = 1)  # two columns of seating capacity w, HN
    df = df.drop(['owner', 'Ownership'], axis = 1) # three columns with ownership data, keeping the one with numerical value
    df = df.drop(['Kms Driven', 'transmission', 'Engine'], axis=1) # two columns with the same data for 3 parameters
    df = df.drop(['Max Torque', 'Max Power', 'Alloy Wheel Size'], axis = 1) # Max Torque has 2 cols of same data, whereas for I have extracted the needed hp.


    return df

def rename_column_names(df):
    """


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

    df = df[['Front Tread', 'Rear Tread']].fillna(value = 0)


    return df

def step2_clean_car_data(df):

    """



    """

    for index, row in df.iterrows():
        s = row['Price in Lakh']
        substring = 'Crore'
        Substring1 = 'Lakh'
        if substring in s:
            s = s.replace('₹', '').replace('Crore', '')
            s = float(s) * 100
            df.loc[index, 'Price in Lakh'] = s
        elif Substring1 in s:
            s = s.replace('₹', '').replace('Lakh', '')
            s = float(s)
            df.loc[index, 'Price in Lakh'] = s
        else:
            s = s.replace(',', '').replace('₹', '')
            s = float(s) / 100000
            df.loc[index, 'Price in Lakh'] = s

    return df

def step3_clean_car_data(df):

    """
    :param df:
    :return: cleaned data:
    removing R from wheel dimensions
    """

    #df['Price in Lakh'] = df['Price in Lakh'].apply(lambda x : x.replace('₹', '').replace('Lakh', ''))
    df['Price in Lakh'] = df['Price in Lakh'].replace('₹', '').replace('Lakh', '')
    df['Wheel Size'] = df['Wheel Size']. apply(lambda x: x.replace('R', ''))

    # engine displacement
    #df['Engine Displacement'] = df['Engine Displacement'].replace('cc', '')
    df['Engine Displacement'] = df['Engine Displacement'].str.extract(r'(\d+)').astype('int')
    #df['Front Tread'] = df['Front Tread'].str.extract(r'(\d+)').astype('int')


    return df



def step4_clean_car_data(df):


    df['Registration Year'] = df['Registration Year'].apply(lambda x : pd.to_datetime(x, format = "mixed"))
    df['Engine Displacement'] = df['Engine Displacement'].astype(int)

    return df