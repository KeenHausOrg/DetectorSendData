import serial

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
sample = ser.read(200) # pull 200 bytes off serial

print(sample)