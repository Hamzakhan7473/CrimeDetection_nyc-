import matplotlib.pyplot as plt

def plot_anomalies(df, save_path='anomalies_map.png'):
    """
    Plot crime data and highlight anomalies.
    """
    anomalies = df[df['anomaly'] == -1]

    plt.figure(figsize=(10, 8))
    plt.scatter(df['lon'], df['lat'], label='Normal', alpha=0.5)
    plt.scatter(anomalies['lon'], anomalies['lat'], color='red', label='Anomalies')
    plt.title('NYC Crime Hotspots and Anomalies')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.legend()
    plt.savefig(save_path)
