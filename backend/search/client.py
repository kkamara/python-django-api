from algoliasearch_django import raw_search

from products.models import Product

# My note:
# At this time (July 2026), AlgoliaSearch is
# 2 versions ahead of the tutorial creator's (v2 -> v4).
# As a result, the API differs considerably.
# V2 can't be used with modern Python / Django. I tried.

def perform_search(query, **kwargs):
    """
    perform_search("hello", tags=["electronics"], public=True)
    """
    params = {}
    tags = ""
    if "tags" in kwargs:
        tags = kwargs.pop("tags") or []
        if 0 != len(tags):
            params["tagFilters"] = tags
    index_filters = [f"{k}:{v}" for k, v in kwargs.items() if v]
    if 0 != len(index_filters):
        params["facetFilters"] = index_filters
    return raw_search(Product, query, params=params)
