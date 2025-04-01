import requests
import pandas as pd
from config.config import NYC_API_URL

def fetch_crime_data(lat, lon, distance=1, limit=100):
    """
    Fetches crime data from the NYC Open Data API.
    """
    # API request parameters
    params = {
        "$limit": limit,
        "$where": f"within_circle(location, {lat}, {lon}, {distance * 1609.34})"
    }

    # Make GET request to NYC Open Data API
    response = requests.get(NYC_API_URL, params=params)

    # Check if request was successful
    if response.status_code == 200:
        data = response.json()

        # Convert data to DataFrame
        if data:
            df = pd.DataFrame(data)
            
            # Extract required data
            if 'location' in df.columns and 'offense' in df.columns:
                df['lat'] = df['location'].apply(lambda x: x.get('latitude') if x else None)
                df['lon'] = df['location'].apply(lambda x: x.get('longitude') if x else None)
                df['offense_type'] = df['offense']

                df.dropna(subset=['lat', 'lon'], inplace=True)
                df['lat'] = df['lat'].astype(float)
                df['lon'] = df['lon'].astype(float)

                return df[['offense_type', 'lat', 'lon']]
        else:
            print("No data found for the given location.")
            return pd.DataFrame()
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return pd.DataFrame()
