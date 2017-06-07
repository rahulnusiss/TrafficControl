import os
import time

static_command = "python Detect.py "
fileLocation = "/home/pi/Desktop/TrafficCongestion/TrafficControl/image_{0}.jpg "
routeNo = "Route{0} "
configFile = "/home/pi/Desktop/TrafficCongestion/TrafficControl/config.json"
for i in range(1,3,1):
    arg1= fileLocation.format(i)
    arg2= routeNo.format(i)
    os.system(static_command + arg1 + arg2 + configFile)
    print("Detect.py called for Route {0}" .format(i))
    time.sleep(5)
