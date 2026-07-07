import requests

endpoint = "https://www.github.com"

get_response = requests.get(endpoint)
print(get_response.text) # print raw text response

# HTTP Request -> HTML
# REST API HTTP Request -> JSON
# JavaScript Object Notation ~ Python Dict

# print(get_response.json())
print(get_response.status_code)
