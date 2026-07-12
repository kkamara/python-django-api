from .models import Product
from rest_framework import serializers
from rest_framework.reverse import reverse


class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    # Displays the full URL for viewing a product.
    # Only works on a `serializers.ModelSerializer`
    url = serializers.HyperlinkedIdentityField(view_name="product_detail", lookup_field="pk")

    class Meta:
        model = Product
        fields = [
            "url",
            "edit_url",
            "pk",
            "title",
            "content",
            "price",
            "sale_price",
            "my_discount",
        ]

    def get_edit_url(self, obj):
        """
        Display the full URL for editing the product.
        """
        request = self.context.get("request") # self.request
        if request is None:
            return None
        return reverse("product_edit", kwargs={"pk": obj.pk}, request=request)

    def get_my_discount(self, obj):
        if not isinstance(obj, Product):
            return None
        return obj.get_discount()

# Tutorial creator's note:
# Maybe we would want a ProductDetailSerializer
# that displays more fields with the view
# method.
