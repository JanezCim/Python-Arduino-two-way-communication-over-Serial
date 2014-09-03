import threading

def Communications:
	coms.run()


if __name__ == '__main__':
	coms = Py2ArdComs()
	t1 = threading.Thread( target=camera, args="" )
	t1.start()