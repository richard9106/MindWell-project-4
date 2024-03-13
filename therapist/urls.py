""" import views and create the url"""

from django.urls import path
from . import views


urlpatterns = [
    path('', views.therapilist, name="therapists"),
] 