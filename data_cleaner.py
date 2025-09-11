import pandas as pd


def gen_clean_car_data(df, fill_values):

    df = df.drop('trendingText', axis = 1)

    return df


def drop_duplicate_columns(df):

    df = df.drop('Seating Capacity', axis = 1)

def clean_car_data(df):

    """
    :param df:
    :return: cleaned data:
    removing R from wheel dimensions
    """
    df['Wheel Size'] = df['Wheel Size']. apply(lambda x: x.replace('R', ''))

    return df

