""" view from home page"""

from django.shortcuts import render


# Create your views here.
def index(request):
    """Home page View"""
    return render(request, 'index.html')
