from twilio.rest import Client
from ConfigManager import ConfigManager 


# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
configs = ConfigManager()
account_sid = configs.TWILIO_ACCOUNT_SID
auth_token = configs.TWILIO_SECRET
apiKeySID = configs.TWILIO_APIKEY
client = Client(apiKeySID,auth_token, account_sid)


message = client.messages \
    .create(
        body='This is the ship that made the Kessel Run in fourteen parsecs?',
        from_='+18563419116',
        to='+14692545597',
        media_url=['https://i.imgur.com/iCekeZX.jpeg'],
     )

print(message)
