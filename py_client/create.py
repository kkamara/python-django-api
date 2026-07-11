import requests

headers = {'Authorization': 'Bearer 1a53935feb345a3505e4f8725a467f95b1660ddf'}
endpoint = "http://localhost:8000/api/products/"

get_response = requests.post(endpoint, json={
    "title": "This field is done",
    "price": 32.99,
}, headers=headers)
print(get_response.json())
