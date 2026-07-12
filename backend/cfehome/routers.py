# Tutorial creator's note:
# Normally, the tutorial creator would
# put everything in urls.py but he
# wanted to separate out the viewsets
# and routers, specifically.
from rest_framework.routers import DefaultRouter
from products.viewsets import ProductGenericViewSet

router = DefaultRouter()
router.register("products", ProductGenericViewSet, basename="products")
urlpatterns = router.urls

# Tutorial creator's note:
# The reason he doesn't use viewsets very often is
# because of how to routing ends up working.
# Router.urls doesn't give him the granular control
# he personally likes his URLs.
# He likes declaring exactly what his URLs are and
# where they go.

# My note:
# Also, using a viewset defaults view methods to
# unrestricted; accessible by everyone including
# unauthenticated users, unless you explicitly
# set permissions on the viewset or globally
# in settings.py.
