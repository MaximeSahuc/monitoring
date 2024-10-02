import requests
import json

try:
    response_API = requests.get('http://127.0.0.1:8081/status')
    response_API.raise_for_status()
    print(response_API.json())
except requests.exceptions.HTTPError as err:
    raise SystemExit(err)
