""" import views and create the url for about"""

from django.urls import path
from . import views


urlpatterns = [
    path('', views.about, name="about")
]
