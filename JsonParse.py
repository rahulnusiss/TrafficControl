import json
from pprint import pprint

with open('config.json') as data_file:    
    data = json.load(data_file)
    print ( data['Route1'] )
    print ( data['Route2'] )

pprint(data)
