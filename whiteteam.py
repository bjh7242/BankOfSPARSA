import requests
import json
import sys # for testing

url = "http://127.0.0.1:5000"

args = {}
args['username'] = "ists_whiteteam"
loc = "/getSecondFactor"
response = requests.post(url+loc,data=args)
decodedOut = json.loads(response.text)

if isinstance(decodedOut, dict):
	print decodedOut['SessionID']
else:
	print decodedOut



