import serial, time

arduino = serial.Serial("COM3", 9600, timeout = 1)
a = 0
time.sleep(1) #give the connection a second to settle


def ArComs():
	data = arduino.readline()[:-2] #the last bit gets rid of the new-line chars
	if data:
		print data
		#print data
		arduino.write("ok")


while True:
	a = a+1
	ArComs()			
	if a>100:
		break