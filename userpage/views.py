""" view when the user is Auth."""

from django.shortcuts import render


# Create your views here.
def singupmodel(request):
    """render the singup"""
    return render(request, 'signup.html')


def userpage(request):
    """dashboard  View when user is auth."""
    return render(request, 'userpage.html')
