import pandas as pd


def gen_clean_car_data(df, fill_values):

    df = df.drop('it', axis=1)

    df = df.drop('trendingText', axis = 1)
    df = df.drop(['priceFixedText', 'centralVariantId'], axis=1)
    df = df.drop('Fabric Upholstery', axis=1) # drop the corollary, leather seat and fabric seat upholstery.
    #df = df.drop('Drive Modes', axis=1) # yes or no, and doesn't make sense, hence can be removed
    df = df.drop('Manually Adjustable Exterior REar View Mirror', axis=1) # dropping the corollary for Power controlled REar view Mirror


    return df



def drop_duplicate_columns(df):

    df = df.drop('Seats', axis = 1)  # two columns of seating capacity w, HN
    df = df.drop(['owner', 'Ownership'], axis = 1) # three columns with ownership data, keeping the one with numerical value
    df = df.drop(['Kms Driven', 'transmission', 'Engine'], axis=1) # two columns with the same data for 3 parameters
    df = df.drop()

    return df

def rename_column_names(df):
    """


    """
    df = df.rename({'ft' : 'Fuel Type', 'bt' : 'Body Type', 'OwnerNo' : 'Ownership No'})
    df = df.rename({'OwnerNo': 'Ownership No'})
    df = df.rename({'km': 'Kilometer Driven'})
    df = df.rename({'oem': 'Original Equipment Manufacturers',
                    'modelYear': 'Model Year',
                    'variantName' : 'Car Variant Details'})

    return df



def clean_car_data(df):

    """
    :param df:
    :return: cleaned data:
    removing R from wheel dimensions
    """
    df['Wheel Size'] = df['Wheel Size']. apply(lambda x: x.replace('R', ''))
    df['Registration Year'] = df['Registration Year'].apply(lambda x : pd.to_datetime(x, format = "mixed"))

    return df

