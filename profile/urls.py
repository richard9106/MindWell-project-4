""" import views and create the url for user page"""

from django.urls import path
from . import views


urlpatterns = [
    path('', views.profile, name="profile"),
    path('delete/', views.delete_profile, name="delete_profile"),
    path('my_appointments/', views.my_appointments, name="my_appointments")
]
