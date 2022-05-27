#!/usr/bin/env python3


import requests
import yaml

#api url to get
APIURL = "http://127.0.0.1:2224/api"

#retrieves the data from the api
houseWives = requests.get(APIURL)

#gets the requested data in JSON format
houseWives = houseWives.json()

#normalizes the JSON into yaml
yamlString = yaml.dump(houseWives)
print(yamlString)
