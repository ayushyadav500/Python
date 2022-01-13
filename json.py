import requests
r = requests.get("http://api.open-notify.org/iss-now.json")
json = r.json
print(json)