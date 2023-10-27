#!/usr/bin/python
import os, sys
import serial
import time

ser = serial.Serial('/dev/ttyUSB0',19200, timeout = 5)

# listen for the input, exit if nothing received in timeout period
while True:
   line = ser.readline()
   if len(line) == 0:
      print("Time out! Exit.\n")
      sys.exit()
   print(line),
