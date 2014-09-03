import serial, time


class Py2ArdComs:
	ThreadRun = 1
	Testing = 0
	Count = 0
	arduino = serial.Serial("COM3", 9600, timeout = 1)
	FromArduinoData = 0

	def __init__(self):
		time.sleep(1) #give the connection a second to settle


	def stop(self):
		self.ThreadRun = 0

	def FromArduino(self):
		return self.FromArduinoData 


	def run(self):
		while (self.ThreadRun):
		#if Testing mode is on, this takes care that the program does not run forever	
			if(self.Testing):
				self.Count = self.Count+1
				if(self.Count>100):
					self.ThreadRun = 0

			data = self.arduino.readline()[:-2] #the last bit gets rid of the new-line chars
			if data:
				self.FromArduinoData = data
				self.arduino.write("ok")
		print("Exiting the coms protocol...")			

if __name__ == '__main__':
	coms = Py2ArdComs()
	coms.run()