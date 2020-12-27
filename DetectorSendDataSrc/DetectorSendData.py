import serial
import requests
import json


multipart_form_data = {
    'image': ('aviation.jpg', open(r"C:/Users/cc/Desktop/aviation.jpg", "rb")),
    'type': (None, 'file'),
    'name': (None, 'aviation.jpg'),
    'title': (None, 'title desc')
}

headers = {'Authorization': 'Bearer 5eeae49394cd929e299785c8805bd168fc675280'}

response = requests.post('https://api.imgur.com/3/upload', files=multipart_form_data,  headers=headers)
print(response.content)

responseObj = json.loads(response.content)
print(responseObj['data']['link'])

# ---- disabled during debug of img uploading ----

# ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=5)
# sample = ser.read(200) # pull 200 bytes off serial

# sample_list = sample.decode('utf-8').split('\n')
# print("sample list var:",sample_list)

# readings = {
#   "Percent": []
# }

# for reading in sample_list:
#   print("working on:" + reading)
#   if '\r' not in reading:
#     break
#   reading = reading.strip()
#   reading_kv = reading.split(':')

#   print("reading var:" + reading)
#   print("kv var:")
#   print(reading_kv)

#   if len(reading) == 2:
#     key = reading_kv[0]
#     val = reading_kv[1]

#     if key == "Percent":
#       readings["Percent"].append(int(val))
