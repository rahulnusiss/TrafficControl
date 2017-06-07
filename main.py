import os
import time

static_command = "python Detect.py "
fileLocation = "/home/pi/Desktop/TafficCongestion/TrafficControl/image_{0} "
routeNo = "route{0}"
for i in range(1,5,1):
    arg1= fileLocation.format(i)
    arg2= routeNo.format(i)
    os.system(static_command + arg1 + arg2 )
    print("Detect.py called for Route {0}" .format(i))
    time.sleep(5)