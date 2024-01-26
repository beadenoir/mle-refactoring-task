import pandas as pd
import numpy as np

def drop_bedroom_outlier(df:pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.drop(df[df['bedrooms'] == 33].index, inplace = True)
    return df

def replace_basement_questionmark(df:pd.DataFrame) -> pd.DataFrame:
    df['sqft_basement'] = df['sqft_basement'].replace('?', np.NaN)
    df['sqft_basement'] = df['sqft_basement'].astype(float)
    return df

def recalculate_basement(df:pd.DataFrame) -> pd.DataFrame:
    df.eval('sqft_basement = sqft_living - sqft_above', inplace=True)
    return df

def fill_nan_with_zero(df:pd.DataFrame) -> pd.DataFrame:
    for column_name in ['view', 
                       'waterfront'
                       ]:
        df.fillna({column_name:0}, inplace=True)
    return df

def create_last_change(df:pd.DataFrame) -> pd.DataFrame:
    last_change = []
    for idx, yr_re in df['yr_renovated'].items():
        if str(yr_re) == 'nan' or yr_re == 0.0:
            last_change.append(df['yr_built'][idx])
        else:
            last_change.append(int(yr_re))
    df['last_change'] = last_change
    return df

def create_distance_to_citycenter(df:pd.DataFrame) -> pd.DataFrame:
    df['delta_lat'] = np.absolute(47.62774- df['lat'])
    df['delta_long'] = np.absolute(-122.24194-df['long'])
    df['center_distance']= ((df['delta_long']* np.cos(np.radians(47.6219)))**2 
                                   + df['delta_lat']**2)**(1/2)*2*np.pi*6378/360
    return df

def dist(long, lat, ref_long, ref_lat):
    delta_long = long - ref_long
    delta_lat = lat - ref_lat
    delta_long_corr = delta_long * np.cos(np.radians(ref_lat))
    return ((delta_long_corr)**2 +(delta_lat)**2)**(1/2)*2*np.pi*6378/360

def create_distance_to_waterfront(df:pd.DataFrame) -> pd.DataFrame:
    water_list= df.query('waterfront == 1')
    water_distance = []
    for idx, lat in df.lat.items():
        ref_list = []
        for x,y in zip(list(water_list.long), list(water_list.lat)):
            ref_list.append(dist(df.long[idx], df.lat[idx],x,y).min())
        water_distance.append(min(ref_list))
    df['water_distance'] = water_distance
    return df

def drop_needless_columns(df:pd.DataFrame) -> pd.DataFrame:
    for column_name in ['yr_renovated', 
                       'yr_built', 
                       'delta_lat', 
                       'delta_long', 
                       'date'
                       ]:
        df.drop(column_name, axis=1, inplace=True, errors='ignore')
    return df