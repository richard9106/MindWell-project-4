""" view from home page"""

from django.shortcuts import render
from allauth.account.forms import SignupForm
from django.contrib.auth import login, authenticate


# Create your views here.
def index(request):
    """Home page View"""
    return render(request, 'index.html', {'form': SignupForm})


def login_view(request):
    """ confir login user"""
    if request.POST.get == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username,
                            password=password)
        if user is None:
            context = {"error": "You must have a User name"}
            return render(request, "account/login.html", context)
