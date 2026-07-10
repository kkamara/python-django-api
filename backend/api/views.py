from products.models import Product
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import ProductSerializer


@api_view(["POST"])
def api_home(request, *args, **kwargs):
    """
    DRF API View
    """
    serialiser = ProductSerializer(data=request.data)
    if serialiser.is_valid(raise_exception=True):
        # instance = serialiser.save()
        # instance = form.save() # Django Form
        print(serialiser.data)
        return Response(serialiser.data)
