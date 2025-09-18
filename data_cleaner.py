import pandas as pd


def gen_clean_car_data(df, fill_values):

    df = df.drop('trendingText', axis = 1)
    df = df.drop('it', axis = 1)

    return df


def rename_column_names(df):
    """


    """
    df = df.rename({'ft' : 'Fuel Type', 'bt' : 'Body Type', 'OwnerNo' : 'Ownership No'})

    return df



def drop_duplicate_columns(df):

    df = df.drop('Seats', axis = 1)  # two columns of seating capacity w, HN
    df = df.drop(['owner', 'Ownership'], axis = 1) # three columns with ownership data, keeping the one with numerical value
    #df = df.drop('ownerNo', 'Ownership', axis=1)
    return df

def clean_car_data(df):

    """
    :param df:
    :return: cleaned data:
    removing R from wheel dimensions
    """
    df['Wheel Size'] = df['Wheel Size']. apply(lambda x: x.replace('R', ''))

    return df

