""" import views and create the url for user page"""

from django.urls import path
from . import views


urlpatterns = [
    path('', views.profile, name="profile"),
    path('delete/', views.delete_profile, name="delete_profile"),
    path('edit_appointment/<str:pk>', views.edit_appointment, name="edit_appointment"),
    path('delete_appointment/<str:pk>', views.delete_appointment, name="delete_appointment")
]
