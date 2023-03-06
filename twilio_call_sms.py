from twilio.rest import Client

# Your Account SID and Auth Token from twilio.com/console
account_sid = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
auth_token = 'your_auth_token'

client = Client(account_sid, auth_token)

# Your Twilio phone number
from_number = '+15017122661'

# The URL of a TwiML document that contains instructions for the call
url = 'http://demo.twilio.com/docs/voice.xml'

def make_call(to_number):
    # This function takes a phone number as an argument and makes a phone call using Twilio
    call = client.calls.create(
        from_=from_number,
        to=to_number,
        url=url
    )
    print(call.sid)


def send_sms(to_number, message):
    # This function takes a phone number and a message as arguments and sends a text message using Twilio
    sms = client.messages.create(
        from_=from_number,
        to=to_number,
        body=message
    )
    print(sms.sid)

