import serial
ser = serial.Serial("/dev/ttyACM0",115200)
while 1 :
	a = ser.readline()
	for s in a.split():
		if s.isdigit():
			print int(s)
	
