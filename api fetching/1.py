import requests  # used to send http requests form python

response = requests.get('https://randomuser.me/api')  # sends HTTP request
print(response.status_code)
data = response.json()  # extracts data in json format
gender = data['results'][0]['gender']
print(gender)