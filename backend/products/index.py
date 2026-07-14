from algoliasearch_django import AlgoliaIndex
from algoliasearch_django.decorators import register
from .models import Product


@register(Product)
class ProductIndex(AlgoliaIndex):
    # should_index = "is_public"
    # Index primitive fields only; related model objects are not JSON-serializable.
    fields = ("title", "body", "price", "username", "public", "path", "endpoint")
    settings = {
        "searchableAttributes": ["title", "body"],
        "attributesForFaceting": ["username", "public"],
    }
    tags = "get_tags_list"
