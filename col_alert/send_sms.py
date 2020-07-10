from twilio.rest import Client


def send(user_sid, user_aid, phone, twilio_phone, message):
    client = Client(user_sid, user_aid)

    client.messages.create(to=phone, # number you signed up with Twilio
                           from_=twilio_phone, # Twilio number
                           body=message)