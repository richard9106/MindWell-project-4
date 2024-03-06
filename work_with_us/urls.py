""" import views and create the url"""

from django.urls import path
from . import views


urlpatterns = [
    path('', views.work_with_us, name="work_with_us"),
]
