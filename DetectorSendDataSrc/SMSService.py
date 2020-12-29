from twilio.rest import Client
from ConfigManager import ConfigManager 

class SMSService:
  def SendMMS(self, message, imageLink):
    configs = ConfigManager()
    account_sid = configs.TWILIO_ACCOUNT_SID
    auth_token = configs.TWILIO_SECRET
    apiKeySID = configs.TWILIO_APIKEY
    client = Client(apiKeySID,auth_token, account_sid)

    message = client.messages \
        .create(
            body=message,
            from_='+18563419116',
            to='+14692545597',
            media_url=[imageLink],
        )
    print(message, imageLink)
