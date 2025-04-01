// Handle form submission and call API
document.getElementById('crimeForm').addEventListener('submit', function (event) {
    event.preventDefault();

    const lat = document.getElementById('lat').value;
    const lon = document.getElementById('lon').value;
    const phone_number = document.getElementById('phone_number').value;

    // Send request to Flask API
    fetch('/detect_crime', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            lat: parseFloat(lat),
            lon: parseFloat(lon),
            phone_number: phone_number
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === "Detection Complete") {
            document.getElementById('result').innerHTML = `<p>Crime detection completed. Anomalies detected: ${data.anomalies.length}</p>`;
            document.getElementById('crimeMap').src = data.map_url;
        } else {
            document.getElementById('result').innerHTML = `<p>No data found for the provided location.</p>`;
        }
    })
    .catch(err => {
        console.error("Error:", err);
        document.getElementById('result').innerHTML = `<p>Failed to fetch crime data. Try again.</p>`;
    });
});
