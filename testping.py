import serial

ser2 = serial.Serial('COM2')
print ser2.read(5)
