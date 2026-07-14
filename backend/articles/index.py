from algoliasearch_django import AlgoliaIndex
from algoliasearch_django.decorators import register


from .models import Article


@register(Article)
class ArticleIndex(AlgoliaIndex):
    should_index = "is_public"
    fields = [
        "title",
        "body",
        "username",
        ("algolia_publish_date", "publish_date"),
        "path",
        "endpoint",
    ]
    settings = {
        "searchableAttributes": ["title", "body"],
        "attributesForFaceting": ["username"],
        "ranking": ["asc(publish_date)"],
    }
    tags = "get_tags_list"
