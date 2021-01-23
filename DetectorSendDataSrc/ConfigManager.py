import json

class ConfigManager:
  TWILIO_ACCOUNT_SID = ""
  TWILIO_SECRET = ""
  TWILIO_APIKEY = ""
  TWILIO_RECEIVERNUMBER = ""
  TWILIO_SENDERNUMBER = ""
  IMGUR_BEARERTOKEN = ""
  IMGUR_APIURL = ""

  def __init__(self):
    with open('ChrisSecrets.json') as f:
      data = json.load(f)
    self.TWILIO_ACCOUNT_SID = data['twilio']['AccountSID']
    self.TWILIO_SECRET = data['twilio']['Secret']
    self.TWILIO_APIKEY = data['twilio']['APIKey']
    self.TWILIO_RECEIVERNUMBER = data['twilio']['ReceiverPhone']
    self.TWILIO_SENDERNUMBER = data['twilio']['SenderPhone']
    self.IMGUR_APIURL = data['imgur']['ApiUrl']
    self.IMGUR_BEARERTOKEN = data['imgur']['BearerToken']
    
