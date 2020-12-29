import json

class ConfigManager:
  TWILIO_ACCOUNT_SID = ""
  TWILIO_SECRET = ""
  TWILIO_APIKEY = ""
  def __init__(self):
    with open('appSettings.json') as f:
      data = json.load(f)
    self.TWILIO_ACCOUNT_SID = data['twilio']['AccountSID']
    self.TWILIO_SECRET = data['twilio']['Secret']
    self.TWILIO_APIKEY = data['twilio']['APIKey']
