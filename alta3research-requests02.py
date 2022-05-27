#!/usr/bin/env python3


import requests
from flask import jsonify


#api url to get
APIURL = "http://127.0.0.1:2224/api"


houseWives = requests.get(APIURL)
houseWives = jsonify(houseWives)


print(houseWives);



#send a GET request to your Flask JSON API and returns legal JSON.

#take the returned JSON and "normalize" it into a format that is easy for users to understand.