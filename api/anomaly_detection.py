from sklearn.ensemble import IsolationForest

def detect_anomalies(df):
    """
    Detect anomalies in crime data using Isolation Forest.
    """
    X = df[['lat', 'lon']]
    
    # Train Isolation Forest model
    model = IsolationForest(n_estimators=100, contamination=0.01, random_state=42)
    df['anomaly'] = model.fit_predict(X)

    # Filter anomalies
    anomalies = df[df['anomaly'] == -1]
    return anomalies
