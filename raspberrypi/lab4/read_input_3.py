import serial
ser=serial.Serial('/dev/ttyUSB0',9600)
while True:
    readedText = ser.readline()
    print(readedText)
ser.close()
