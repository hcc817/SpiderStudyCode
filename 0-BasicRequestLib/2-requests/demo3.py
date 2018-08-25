import requests

data = {
    'name': 'mtianyan',
    'age': 21
}
r = requests.get("http://httpbin.org/get", params=data)
print(r.text)