import serial, time


class Py2ArdComs:
	arduino = serial.Serial("COM3", 9600, timeout = 1)
	time.sleep(1) #give the connection a second to settle


	def run(self):
		a = 0
		while True:
			a = a+1
			data = self.arduino.readline()[:-2] #the last bit gets rid of the new-line chars
			if data:
				print data
				#print data
				self.arduino.write("ok")			
			if a>100:
				break

if __name__ == '__main__':
	coms = Py2ArdComs()
	coms.run()