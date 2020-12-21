import serial

ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=5)
sample = ser.read(200) # pull 200 bytes off serial

sample_list = sample.decode('utf-8').split('\n')
print("sample list var:",sample_list)

readings = {
  "moisture": []
}

for reading in sample_list:
  print("working on:" + reading)
  if '\r' not in reading:
    break
  reading = reading.strip()
  reading_kv = reading.split(':')

  print("reading var:" + reading)
  print("kv var:")
  print(reading_kv)

  if len(reading) == 2:
    key = reading_kv[0]
    val = reading_kv[1]

    if key == "moisture":
      readings["moisture"].append(int(val))
