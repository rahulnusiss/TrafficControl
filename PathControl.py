import time
import Relay
import json

class Route:
	'This class represents root at a junction'
	
	def __init__(self, name, isOpen, density, light1, light2):
		self.name = name
		self.isOpen = isOpen
		self.density = density
		self.light1 = light1
		self.light2 = light2
		
		
	def showStatus(self):
		print "Name : ", self.name, ", Status: ", self.isOpen, ", Density: ", self.density
		
	def changeStatus(self):
		if self.isOpen == True:
			self.isOpen = False
		else:
			self.isOpen = True		
		
	def startRoute(self):
		self.isOpen = True;
		Relay.startFunc(self.light1,1)
		Relay.startFunc(self.light2,1)
		
	def stopRoute(self):
		self.isOpen = False;
		Relay.startFunc(self.light1,0)
		Relay.startFunc(self.light2,0)		
		
		
#Test function for relay control
def startRelay1(routeNumber):
	if 1 == routeNumber:
		# Relay input 1,3 On
		Relay.startFunc(0,1)
		Relay.startFunc(2,1)
		time.sleep(5)
		# Relay input 1,3 Off
		Relay.startFunc(0,0)
		Relay.startFunc(2,0)
		startRelay(2)
	else:
		# Relay input 2,4 On
		Relay.startFunc(1,1)
		Relay.startFunc(3,1)
		time.sleep(5)
		# Relay input 2,4 Off
		Relay.startFunc(1,0)
		Relay.startFunc(3,0)
		startRelay(1)
		

# Actual IOT Relay Control
def startRelay(route1, route2):
	minTime = 10
	maxTime = 20
	timeCounter = minTime-5
	if True == route1.isOpen:
		# Relay input 1,3 On
		route1.startRoute();
		time.sleep(timeCounter)
		while(timeCounter < maxTime):
			data = readConfig()
			if data['Route1'] == 1:
				print("Route 1 open ", timeCounter, "seconds")
				timeCounter = timeCounter+2
				if timeCounter+5 >= maxTime:
					print("Stopping route 1 in 5 seconds")
					time.sleep(5)
					break
				else:
					time.sleep(2)
					
			else:
				print("Stopping route 1 in 5 seconds")
				time.sleep(5)
				break;		
		# Relay input 1,3 Off
		route1.stopRoute();		
		startRelay(route1,route2)
		
	else:
		# Relay input 2,4 On
		timeCounter = minTime-5
		route2.startRoute();
		time.sleep(timeCounter)
		while(timeCounter < maxTime):
			data = readConfig()
			if data['Route2'] == 1:
				print("Route 2 open ", timeCounter, "seconds")
				timeCounter = timeCounter+2
				if timeCounter+5 >= maxTime:
					print("Stopping route 2 in 5 seconds")
					time.sleep(5)
					break
				else:
					time.sleep(2)
			else:
				print("Stopping route 2 in 5 seconds")
				time.sleep(5)
				break;				
		# Relay input 2,4 Off
		route2.stopRoute();
		route1.changeStatus()
		startRelay(route1,route2)
		

def readConfig():	
	with open('config.json') as data_file:    
		data = json.load(data_file);
		print("Route1 ", data['Route1'], "Route2 ", data['Route2'] )
	return data;
	
	
def main():
	minTime = 30
	maxTime = 100
	route1 = Route( "Route1", True, 1, 0, 2 )
	route2 = Route( "Route2", False, 0, 1 ,3 )
	route1.density = 1;
	route2.density = 0;
	startRelay(route1, route2)
			
	route1.showStatus()
	route2.showStatus()

if __name__ == "__main__":
    main()
