""" import views and create the url for user page"""

from django.urls import path
from . import views


urlpatterns = [
    path('', views.userpage, name="userpage")
]
