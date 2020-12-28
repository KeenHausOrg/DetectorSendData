from picamera import PiCamera
from datetime import datetime
from time import sleep
import serial
import requests
import json
import numpy as np

# "constants"
_picturePath = '/home/pi/Pictures/'

# Main func
def main():
  print("Starting program ...")
  sleep(1)
  moisturePcnt = ReadSerial()
  phrase = GetPhrase(moisturePcnt)
  pictureName = TakePicture()

  print("moisture: ", moisturePcnt)
  print("phrase: ", phrase)
  print("pic: ", pictureName)

  #UploadPicture(pictureName)

  # ---- disabled during debug of img uploading ----
def ReadSerial():
  ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=5)
  sample = ser.read(200) # pull 200 bytes off serial

  sample_list = sample.decode('utf-8').split('\n')
  print("sample list var:",sample_list)

  readings = {
    "Percent": []
  }

  for reading in sample_list:
    print("working on:" + reading)
    if '\r' not in reading:
      break
    reading = reading.strip()
    reading_kv = reading.split(':')

    print("kv var:")
    print(reading_kv)

    if len(reading_kv) == 2:
      key = reading_kv[0]
      val = reading_kv[1]

      if key == "Percent":
        print("val to be inserted into array: ", int(val))
        readings["Percent"].append(int(val))

  print("pcnt array : ", readings["Percent"])
  if(len(readings["Percent"]) > 0):
    average = np.average(readings["Percent"])
    return average
  else:
    return -1

def TakePicture():
  camera = PiCamera()
  camera.start_preview()
  sleep(4)
  now = datetime.now() # current date and time
  date_time = now.strftime("%m%d%Y_%H%M%S")
  fileName = 'plantcam_'+date_time+'.jpg'
  camera.capture(_picturePath+fileName)
  camera.stop_preview()
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
  multipart_form_data = {
      'image': ('aviation.jpg', open(r"C:/Users/cc/Desktop/aviation.jpg", "rb")),
      'type': (None, 'file'),
      'name': (None, 'aviation.jpg'),
      'title': (None, 'title desc')
  }
  headers = {'Authorization': 'Bearer 5eeae49394cd929e299785c8805bd168fc675280'}

  response = requests.post('https://api.imgur.com/3/upload', files=multipart_form_data,  headers=headers)
  print(response.content)

  # deal with the response
  responseObj = json.loads(response.content)
  successStatus = responseObj['success']

  if (successStatus == True):
    imgurLink = responseObj['data']['link']
  else:
    imgurLink = "error"

if __name__ == '__main__':
  main()