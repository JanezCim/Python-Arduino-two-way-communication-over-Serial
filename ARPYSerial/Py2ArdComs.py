import serial, time


class Py2ArdComs:
	Testing = 0
	ThreadRun = 1
	Count = 0
	arduino = serial.Serial("COM3", 9600, timeout = 1)
	FromArduinoData = 0
	ToArduinoData = "ok"

	def __init__(self):
		time.sleep(1) #give the connection a second to settle


	def stop(self):
		self.ThreadRun = 0

	def FromArduino(self, toArduinoData):
		self.ToArduinoData = toArduinoData
		return self.FromArduinoData 

	def run(self):
		data = 0
		while (self.ThreadRun):
		#if Testing mode is on, this takes care that the program does not run forever	
			if(self.Testing):
				print data
				self.Count = self.Count+1
				if(self.Count>100):
					self.ThreadRun = 0

			data = self.arduino.readline()[:-2] #the last bit gets rid of the new-line chars
			if data:
				self.FromArduinoData = data
				self.arduino.write(self.ToArduinoData)
		print("Exiting the coms protocol...")			

if __name__ == '__main__':
	coms = Py2ArdComs()
	coms.run()