import numpy as np
import pandas as pd

def remove_outliers_class(df):

    index_to_remove = df[df['Number of Outliers'] != 0]

    df.drop(index_to_remove.index, inplace=True)

    df.reset_index(drop=True, inplace=True)

    return df

def classify_outliers(df):

    ranges = {}

    ranges['CALI'] = [5, 30]

    ranges['NPHI'] = [0.1, 0.65] 

    ranges['RHOB'] = [1, 3.5] 

    ranges['GR'] = [0, 200]

    ranges['DTC'] = [40, 200]

    ranges['RDEP'] = [0.0001, 6000]

    ranges['RMED'] = [0.0001, 6000] 

    for curve in df.columns:
        for idx in df.index:
            if curve not in ['Number of Outliers', 'LITHOLOGY_GEOLINK', 'WELL_NAME', 'DEPTH']:
                if (df[curve][idx] < ranges[curve][0]) or (df[curve][idx] > ranges[curve][1]):

                    df.at[idx, 'Number of Outliers'] = df['Number of Outliers'][idx] + 1

    return df 

def nphi_filtering(df):

    for id in df['WELL_NAME'].unique():

        mean = df[df['WELL_NAME'] == id]['NPHI'].mean()
            
        if mean > 1:

            df.loc[df['WELL_NAME'] == id,['NPHI']] = df.loc[df['WELL_NAME'] == id,['NPHI']]/100

        else:

            for idx in df[df['WELL_NAME'] == id].index:

                if df[df['WELL_NAME'] == id]['NPHI'][idx] > 1:
                    
                    df[df['WELL_NAME'] == id].drop(index=idx, inplace=True)

    return df
