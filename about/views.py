""" view from home page"""

from django.shortcuts import render


# Create your views here.
def about(request):
    """about page View"""
    return render(request, 'about.html')
