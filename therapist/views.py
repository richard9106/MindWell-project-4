""" Therapist Views"""

from django.shortcuts import render
from django.views import generic
from .models import Therapists


# Create your views here.
class TherapiList(generic.ListView):
    """View for list therapists"""
    queryset = Therapists.objects.all()
    template_name = "therapist_list.html"
