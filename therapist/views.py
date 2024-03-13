""" Therapist Views"""

from django.shortcuts import render
from .models import Therapists


# Create your views here.
def therapilist(request):
    """View for list therapists"""
    therapists = Therapists.objects.all()
    
    return render(request, "therapist_list.html",
                  {'therapists': therapists})


