import requests
from getpass import getpass

auth_endpoint = "http://localhost:8000/api/auth/"
username = input("What is your username?\n>> ")
password = getpass("Enter password:\n>> ")

get_response = requests.post(
    auth_endpoint,
    json={
        "username": username,
        "password": password,
    },
)
print(get_response.json())


if 200 == get_response.status_code:
    token = get_response.json().get("token")
    headers = {"Authorization": f"Bearer {token}"}
    endpoint = "http://localhost:8000/api/products/"

    get_response = requests.get(endpoint, headers=headers)
    print(get_response.json())
