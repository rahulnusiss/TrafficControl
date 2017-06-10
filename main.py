import os
import time
from paho.mqtt.client import Client
import datetime
import json

static_command = "python Detect.py "
congestedImage = "/home/pi/Desktop/TrafficCongestion/TrafficControl/resources/congested.jpg "
notCongestedImage = "/home/pi/Desktop/TrafficCongestion/TrafficControl/resources/not_congested.jpg "
routeNo = "Route{0} "
configFile = "/home/pi/Desktop/TrafficCongestion/TrafficControl/config/config.json"
client = Client(client_id="my_id_pub", userdata="user2")
client.connect("172.23.135.89")
for i in range(1,5,1):
    if i==1:
        arg1= notCongestedImage
        arg2= notCongestedImage
        print("No congestion on any route")
    if i==2:
        arg1= notCongestedImage
        arg2= congestedImage
        print("congestion on Route 2")
    if i==3:
        arg1= congestedImage
        arg2= notCongestedImage
        print("congestion on Route 1")
    if i==4:
        arg1= congestedImage
        arg2= congestedImage
        print("congestion on both Route ")
        
    os.system(static_command + arg1 + arg2 + configFile)
    
    with open(configFile) as data_file:
        data = json.load(data_file)
        #print data[arg2]
    topic = "temp"
    message = "{  \"Route1\" : " + str(data['Route1']) + " , \"Route2\" : " + str(data['Route2']) +" }"

    print message
    client.publish(topic, message)  
    time.sleep(3)



  
