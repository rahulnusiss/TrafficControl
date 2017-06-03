import time
import Relay

class Route:
	'This class represents root at a junction'
	
	def __init__(self, name, isOpen, density):
		self.name = name
		self.isOpen = isOpen
		self.density = density
		
	def showStatus(self):
		print "Name : ", self.name, ", Status: ", self.isOpen, ", Density: ", self.density
		
	def changeStatus(self, timeToChange):
		if self.isOpen == True:
			self.isOpen = False
		else:
			self.isOpen = True
		time.sleep(timeToChange)
		

def startRelay(routeNumber):
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
	
	
def main():
	minTime = 30
	maxTime = 100
	route1 = Route( "Route1", True, 1 )
	route2 = Route( "Route2", False, 0 )
	route1.density = 1;
	route2.density = 0;
	startRelay(1)	
			
	route1.showStatus()
	route2.showStatus()

if __name__ == "__main__":
    main()
