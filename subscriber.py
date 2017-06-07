import time
import json
from paho.mqtt.client import Client
 
def on_message(c, userdata, mesg):
	print "message: %s %s %s" % (userdata, mesg.topic, mesg.payload)
	with open('config.json', 'w') as outfile:
		outfile.write(mesg.payload)
		#json.dump(mesg.payload, outfile)

client = Client(client_id="my_id", userdata="user1")
client.connect("172.23.135.89")
client.on_message = on_message
client.subscribe("temp")
while True:
	client.loop()
	time.sleep(1)
