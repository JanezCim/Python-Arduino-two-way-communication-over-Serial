Python-Arduino-two-way-communication-over-Serial
================================================

This is a way for arduino and python to exchange only some variables while still running their own programs.
The communication on arduino is done with simple Serial.read and Serial.write, while on python two different programs are running at the same time. It is done by threading library. 

Py2ArdComs.py takes care of communicating with arduino, while PythonMain.py runs at normal speeds and gets Serial information thru the first one.

I found out that the speed of arduino program is depended of speed of communications and therefore the speed of computer that Arduino is connected to. That's why: 
TODO: make Arduino program run fully indipendet of the device that it's connected to.(Speed if processing)
