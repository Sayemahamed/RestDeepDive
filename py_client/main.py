import requests
endpoint="https://httpbin.org/status/200"
endpoint="https://httpbin.org/anything"

response=requests.get(endpoint ,json={"say":"hi"})
print(response.text)
print(response.status_code)
