from twilio.rest import Client
from django.conf import settings

def send_whatsapp_notification(booking):
    """
    Sends a WhatsApp notification to the admin using Twilio.
    Requires TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_WHATSAPP_NUMBER, and ADMIN_WHATSAPP_NUMBER in settings.
    """
    
    account_sid = getattr(settings, 'TWILIO_ACCOUNT_SID', None)
    auth_token = getattr(settings, 'TWILIO_AUTH_TOKEN', None)
    from_whatsapp = getattr(settings, 'TWILIO_WHATSAPP_NUMBER', 'whatsapp:+14155238886')
    to_whatsapp = getattr(settings, 'ADMIN_WHATSAPP_NUMBER', None)

    if account_sid and auth_token and to_whatsapp:
        try:
            client = Client(account_sid, auth_token)
            
            message = f"""
            🆕 *New Booking Received!*
            
            👤 *User:* {booking.user.username}
            🎉 *Function:* {booking.function_type.name}
            📍 *Venue:* {booking.venue_name}
            📅 *Date:* {booking.date}
            ⏰ *Time:* {booking.time}
            """
            
            client.messages.create(
                body=message,
                from_=from_whatsapp,
                to=to_whatsapp
            )
            print("WhatsApp notification sent successfully.")
        except Exception as e:
            print(f"Failed to send WhatsApp notification: {e}")
    else:
        print("Twilio credentials not configured. Skipping WhatsApp notification.")
    
    # For demonstration purposes
    print(f"--- MOCK NOTIFICATION ---\nNew Booking: {booking.function_type.name} by {booking.user.username}\nVenue: {booking.venue_name}\n-------------------------")
