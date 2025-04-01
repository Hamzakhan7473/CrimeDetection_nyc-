from twilio.rest import Client
from config.config import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER

def send_alert(phone_number, message):
    """
    Sends an SMS alert using Twilio API.
    """
    # Initialize Twilio client
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    try:
        # Send SMS alert
        alert = client.messages.create(
            body=message,
            from_=TWILIO_PHONE_NUMBER,
            to=phone_number
        )
        print(f"✅ Alert Sent! Message SID: {alert.sid}")
        return alert.sid
    except Exception as e:
        print(f"❌ Failed to send alert: {str(e)}")
        return None
