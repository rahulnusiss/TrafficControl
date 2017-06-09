import sys
import json
import os
import logging

def writeData(data):
	print "message: %s " % (data)
	with open("/home/pi/Documents/IOTCA/init.json", 'w') as outfile:
		#json.dump(data, outfile)
		outfile.write(data)

def main():
    if len(sys.argv) > 2:
        #logging.basicConfig(filename='temphumbar',filemode='a',format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',datefmt='%H:%M:%S',level=logging.INFO)
        [cmd,minimum,maximum] = sys.argv
        msgBuffer = "{ \"Min\": " + minimum + " , \"Max\": " + maximum + " } ";
        writeData(msgBuffer);
        print msgBuffer
        return "This is called"
    else:
        print "Minimum, Maximum : %s " % sys.argv[0]
 
if __name__ == "__main__":
    main()
