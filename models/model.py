# models/model.py

from sklearn.ensemble import IsolationForest
import joblib
import pandas as pd

def train_model(df):
    X = df[['lat', 'lon']]
    model = IsolationForest(n_estimators=100, contamination=0.01, random_state=42)
    model.fit(X)
    joblib.dump(model, 'models/crime_detector.pkl')

def load_model():
    model = joblib.load('models/crime_detector.pkl')
    return model
