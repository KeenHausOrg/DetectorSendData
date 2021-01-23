from picamera import PiCamera
from datetime import datetime
from time import sleep
import serial
import requests
import json
import numpy as np
import os
from SMSService import SMSService
from ConfigManager import ConfigManager 

# "constants"
_picturePath = '/home/pi/Pictures/'
_configs = ConfigManager()
# Main func
def main():
  print("Starting program ...")
  smsService = SMSService()
  
  while(1):
    currTime = datetime.now()
    sleep(1)

    if(currTime.hour == 16):
      moisturePcnt = ReadSerial()
      phrase = GetPhrase(moisturePcnt)
      pictureName = TakePicture()
      imgLink = UploadPicture(pictureName)
      smsService.SendMMS(phrase, imgLink)

      print("moisture: ", moisturePcnt)
      print("phrase: ", phrase)
      print("pic: ", pictureName)
      print("link: ", imgLink)

      if (len(imgLink) > 3 and imgLink!='error'):
        if (os.path.exists(_picturePath+pictureName)):
          os.remove(_picturePath+pictureName)
      
      sleep(3599)
    
    else:
      print("Curr hour is ",currTime.hour,". Sleeping for another")
      sleep(3599)


def ReadSerial():
  ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=5)
  sample = ser.read(200) # pull 200 bytes off serial

  sample_list = sample.decode('utf-8').split('\n')
  print("sample list var:",sample_list)

  readings = {
    "Percent": []
  }

  for reading in sample_list:
    if '\r' not in reading:
      break
    reading = reading.strip()
    reading_kv = reading.split(':')

    if len(reading_kv) == 2:
      key = reading_kv[0]
      val = reading_kv[1]

      if key == "Percent":
        readings["Percent"].append(int(val))

  if(len(readings["Percent"]) > 0):
    average = np.average(readings["Percent"])
    return average
  else:
    return -1

def TakePicture():
  fileName="error"
  camera = PiCamera(resolution=(1280,720))
  try:
    camera.rotation = 90
    camera.preview_fullscreen=False
    camera.start_preview()

    sleep(4)
    now = datetime.now() # current date and time
    date_time = now.strftime("%m%d%Y_%H%M%S")
    fileName = 'plantcam_'+date_time+'.jpg'
    camera.capture(_picturePath+fileName, format='jpeg', use_video_port=False, resize=None, bayer=False)
    camera.stop_preview()
  finally:
    camera.close()
    return fileName


def GetPhrase(moisturePcnt):
  errorPhrase = "Moisture reading is invalid."
  wetPhrase = "Soil is wet."
  dryPhrase = "Soild is dry."
  
  if(moisturePcnt < 0):
    return errorPhrase
  elif (moisturePcnt < 50):
    return dryPhrase
  else:
    return wetPhrase

def UploadPicture(pictureName):
# request building
  print("Attempting to upload picture ...")
  multipart_form_data = {
      'image': (pictureName, open(_picturePath+pictureName, "rb")),
      'type': (None, 'file'),
      'name': (None, pictureName),
      'title': (None, 'Automatic picture upload')
  }
  headers = {'Authorization': _configs.IMGUR_BEARERTOKEN}

  response = requests.post(_configs.IMGUR_APIURL, files=multipart_form_data,  headers=headers)
  print("Request response:", response.headers)
  print(response.content)

  # deal with the response
  responseObj = json.loads(response.content)
  successStatus = responseObj['success']

  if (successStatus == True):
    imgurLink = responseObj['data']['link']
  else:
    imgurLink = "error"
  return imgurLink

if __name__ == '__main__':
  main()
