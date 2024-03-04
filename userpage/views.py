""" view when the user is Auth."""

from django.shortcuts import render


# Create your views here.
def userpage(request):
    """dashboard  View when user is auth."""
    return render(request, 'userpage.html')
