# utils/preprocess.py

import pandas as pd

def preprocess_data(df):
    # Drop missing values
    df.dropna(inplace=True)

    # Convert date to datetime format
    df['incident_date'] = pd.to_datetime(df['incident_date'])

    # Select required columns
    df = df[['incident_type', 'incident_date', 'lat', 'lon', 'severity']]
    return df
