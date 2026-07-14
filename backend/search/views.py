from rest_framework import generics

from products.models import Product
from products.serializers import ProductSerializer

from . import client
from rest_framework.response import Response


class SearchListView(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        username = None
        if request.user.is_authenticated:
            username = request.user.username
        query = request.GET.get("q", "")
        public = "0" != request.GET.get("public", "")
        tag = request.GET.get("tag", None)
        # Tutorial creator does this but I won't
        # because a default value is set
        # if not query:
        #     return Response("", status=400)
        results = client.perform_search(
            query, tags=tag, username=username, public=public
        )
        return Response(results)


class SearchListOldView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get("q")
        results = Product.objects.none()
        if q is not None:
            user = None
            if self.request.user.is_authenticated:
                user = self.request.user
            results = qs.search(q, user=user)
        return results
