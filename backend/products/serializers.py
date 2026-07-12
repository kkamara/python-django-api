from .models import Product
from rest_framework import serializers
from rest_framework.reverse import reverse


class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    # Displays the full URL for viewing a product.
    # Only works on a `serializers.ModelSerializer`
    url = serializers.HyperlinkedIdentityField(
        view_name="product_detail", lookup_field="pk"
    )
    # Without write_only it will error because the field is not in the model. It will be used for creating a product.
    # email = serializers.EmailField(write_only=True)

    class Meta:
        model = Product
        fields = [
            "url",
            "edit_url",
            # "email",
            "pk",
            "title",
            "content",
            "price",
            "sale_price",
            "my_discount",
        ]

    # def create(self, validated_data):
    #     # return Product.objects.create(**validated_data)
    #     # email = validated_data.pop("email")
    #     obj = super().create(validated_data)
    #     # print(email, obj)
    #     return obj
    
    # def update(self, instance, validated_data):
    #     # instance.title = validated_data.get("title", instance.title)
    #     # return instance
    #     email = validated_data.pop("email", None) # Just to ensure the email gets removed from `validated_data`
    #     return super().update(instance, validated_data)

    def get_edit_url(self, obj):
        """
        Display the full URL for editing the product.
        """
        request = self.context.get("request")  # self.request
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
