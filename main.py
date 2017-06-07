import os
import time
from paho.mqtt.client import Client
import datetime
import json

static_command = "python Detect.py "
fileLocation = "/home/pi/Desktop/Rahul/TrafficControl/image_{0}.jpg "
routeNo = "Route{0} "
configFile = "//home/pi/Desktop/Rahul/TrafficControl/config.json"
client = Client(client_id="my_id_pub", userdata="user2")
client.connect("172.23.135.89")
for i in range(1,3,1):
    arg1= fileLocation.format(i)
    arg2= routeNo.format(i)
    os.system(static_command + arg1 + arg2 + configFile)
    print("Detect.py called for Route {0}" .format(i))
    with open('config.json') as data_file:
        data = json.load(data_file)
        #print data[arg2]
    topic = "temp"
    message = "{  \"Route1\" : " + str(data['Route1']) + " , \"Route2\" : " + str(data['Route2']) +" }"

    print message
    client.publish(topic, message)  
    time.sleep(10)



  
