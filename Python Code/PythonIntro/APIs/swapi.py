
# # # import requests

# # # base_url = "https://swapi.dev/api/"
# # # endpoint = "people/"
# # # # Response object
# # # response = requests.get(base_url + endpoint)
# # # data = response.json()
# # # print(data['name'])


# import requests

# import json

# base_url =  "https://swapi.info/api/"
# endpoint = "people/"


# # Stored as a a response class object
# response = requests.get(base_url + endpoint)
# data = response.json()

# # print(response)
# # print("Text:")
# # print(response.text)
# # print("Status Code:")   
# # print(response.status_code)
# # print("Headers:")
# # print(response.headers)

# # print(data)
# print(data [0]["name"])



import requests
import json

url = "https://swapi.info/api/starships/3"

payload = {}
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

# ========================================================

import requests
import json

url = "https://swapi.info/api/people/1"

payload = {}
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
