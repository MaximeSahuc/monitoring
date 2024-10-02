import requests
import json

try:
    response_API = requests.get('http://127.0.0.1:8081/status')
    response_API.raise_for_status()
    print(response_API.json())
except requests.exceptions.RequestException as errr:
    print ("OOps: Something Else",errr)
except requests.exceptions.HTTPError as errh:
    print ("Http Error:",errh)
except requests.exceptions.ConnectionError as errc:
    print ("Error Connecting:",errc)
except requests.exceptions.Timeout as errt:
    print ("Timeout Error:",errt)



data=json.load(response_API)
print(data)