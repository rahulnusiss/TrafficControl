import RPi.GPIO as GPIO
import sys
 
class Relay:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        self.pinList = [22,23,24,25]
 
    def switch(self, lamp, state):
        pin = self.pinList[lamp]
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, (GPIO.HIGH if state == 0 else GPIO.LOW))
 
def startFunc(iLamp, iState):
	print " Lamp = ", iLamp, " State = ", iState
		
	lamp = int(iLamp)   # which lamp?
	state = int(iState) # off/on?
		
	if lamp >=0 and lamp <= 3 and (state == 0 or state ==1):
        #[cmd,lamp,state] = sys.argv
		relay = Relay()
		relay.switch(lamp, state)
	else:
		print " Lamp = 0,1,2,3  and state = 0,1"
 
if __name__ == "__main__":	
	if len(sys.argv) > 2:
		[cmd,lamp,state] = sys.argv
		startFunc(lamp, state)
	else:
		print "Usage: %s <relay> <0/1>" % sys.argv[0]
    
