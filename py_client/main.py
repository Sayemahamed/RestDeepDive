import requests
# endpoint="https://httpbin.org/status/200"
endpoint="http://localhost:8000/api/product/?format=json"

response=requests.get(endpoint)
print(response.text)
print(response.status_code)
