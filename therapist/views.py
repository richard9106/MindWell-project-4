""" Therapist Views"""
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Therapists
from .forms import UserAppointmentManager


# Create your views here.
@login_required
def therapilist(request):
    """View for list therapists"""
    therapists = Therapists.objects.all()
    
    return render(request, "therapist_list.html",
                  {'therapists': therapists})


@login_required
def therapist_profile(request, first_name):
    """define the info to display in the therapist profile page"""

    queryset = Therapists.objects.all()
    therapist = get_object_or_404(queryset, first_name=first_name)

    return render(
        request,
        "therapist_profile.html",
        {"therapist": therapist,
         "appointment_form": UserAppointmentManager}
    )

