""" Therapist Views"""

from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def therapists(request):
    """render a list of therapist available"""
    return HttpResponse("Therapists list page")
