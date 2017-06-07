import json
from pprint import pprint

with open('config.json') as data_file:    
    data = json.load(data_file)
    print ( data['Route1'] )
    print ( data['Route2'] )

message = "{  'Route1' : {0} , 'Route2' : {1} }"    
message.format(data["Route1"], data["Route2"])

pprint(message)
