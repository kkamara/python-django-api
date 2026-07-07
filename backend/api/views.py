from django.http import JsonResponse, HttpResponse
import json
from products.models import Product
from django.forms.models import model_to_dict


def api_home(request, *args, **kwargs):
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data = model_to_dict(
            model_data,
            fields=[
                "id",
                "title",
                "price",
            ],
        )
    return JsonResponse(data)
    #     print(data)
    #     data = dict(data)
    #     json_data_str = json.dumps(data)
    #     print(json_data_str)
    # return HttpResponse(json_data_str, headers={"Content-Type": "application/json"})
    # My notes:
    #   The price is a decimal field, so it needs to be converted for JSON serialization.
    #   This is manual work that is tedious and error-prone.
