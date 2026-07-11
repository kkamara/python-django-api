from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('auth/', obtain_auth_token, name='api_token_auth'),
    path('', views.api_home, name='api_home'),
]
