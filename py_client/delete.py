import requests

def getProductId():
    result = input("What is the product ID you want to delete?\n>> ")
    if result is None or result == "" or not result.isdigit():
        print("Invalid product ID")
        return None
    return int(result)

product_id = None
while product_id is None:
    product_id = getProductId()

endpoint = f"http://localhost:8000/api/products/{product_id}/delete/"

get_response = requests.delete(endpoint)
print(get_response.status_code)
