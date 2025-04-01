from flask import render_template
from app import app
from flask import Flask, request, jsonify, render_template
from api.fetch_data import fetch_crime_data
from api.anomaly_detection import detect_anomalies
from api.notify import send_alert
from utils.visualize import plot_anomalies

app = Flask(__name__)

@app.route('/')
def index():
    """Load the main HTML page."""
    return render_template('index.html')


@app.route('/detect_crime', methods=['POST'])
def detect_crime():
    """
    API endpoint to detect crime data and anomalies.
    """
    try:
        # Receive latitude, longitude, and phone number from frontend
        data = request.json
        lat, lon = float(data['lat']), float(data['lon'])
        phone_number = data.get('phone_number')

        # Fetch NYC crime data
        df = fetch_crime_data(lat, lon)
        if df.empty:
            return jsonify({"status": "No data available"})

        # Perform anomaly detection
        anomalies = detect_anomalies(df)

        # Generate map and save visualization
        plot_anomalies(df, 'app/static/anomalies_map.png')

        # Send alert if anomalies are detected
        if not anomalies.empty and phone_number:
            message = f"🚨 Alert! {len(anomalies)} suspicious activities detected in your area. Check the report for details."
            send_alert(phone_number, message)

        # Return JSON response with results
        return jsonify({
            "status": "Detection Complete",
            "anomalies": anomalies.to_dict(orient='records'),
            "map_url": "/static/anomalies_map.png"
        })
    
    except Exception as e:
        return jsonify({"status": "Error", "message": str(e)})
