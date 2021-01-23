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
            from_=configs.TWILIO_SENDERNUMBER,
            to=configs.TWILIO_RECEIVERNUMBER,
            media_url=[imageLink],
        )
    print(message, imageLink)
