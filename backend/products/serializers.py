from .models import Product
from rest_framework import serializers
from rest_framework.reverse import reverse
from . import validators
from api.serializers import UserPublicSerializer


class ProductInlineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="product_detail", lookup_field="pk", read_only=True
    )
    title = serializers.CharField(read_only=True)


class ProductSerializer(serializers.ModelSerializer):
    owner = UserPublicSerializer(source="user", read_only=True)
    # edit_url = serializers.SerializerMethodField(read_only=True)
    # Displays the full URL for viewing a product.
    # Only works on a `serializers.ModelSerializer`
    # url = serializers.HyperlinkedIdentityField(
    #     view_name="product_detail", lookup_field="pk"
    # )
    title = serializers.CharField(
        validators=[validators.validate_title_no_hello, validators.unique_product_title]
    )
    body = serializers.CharField(source="content")

    class Meta:
        model = Product
        fields = [
            "pk",
            "title",
            "body",
            "price",
            "sale_price",
            "owner",
            "public",
            "path",
            "endpoint",
        ]

    # def get_edit_url(self, obj):
    #     """
    #     Display the full URL for editing the product.
    #     I have tested and you could replicate this
    #     with HyperlinkedIdentityField like the url
    #     property.
    #     """
    #     request = self.context.get("request")  # self.request
    #     if request is None:
    #         return None
    #     return reverse("product_edit", kwargs={"pk": obj.pk}, request=request)

    # My note:
    # The tutorial creator and I removed the code examples
    # for declaring methods validate_title, create, and
    # update. This note serves as in-place documentation.
