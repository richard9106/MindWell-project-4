""" Therapist Views"""
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User
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

    if request.method == 'POST':
        appointment_form = UserAppointmentManager(request.POST)
        if appointment_form.is_valid():
            instance = appointment_form.save(commit=False)
            instance.client = User.objects.get(username=request.user.username)
            instance.therapist = Therapists.objects.get(first_name=first_name)
            instance.save()

            messages.add_message(
                request,
                messages.SUCCESS,
                "Your appointment was successfully register")
            return HttpResponseRedirect(reverse('profile'))
        else:
            messages.add_message(
                request,
                messages.WARNING,
                "Something has gone wrong select an other day")

    return render(
        request,
        "therapist_profile.html",
        {"therapist": therapist,
         "appointment_form": UserAppointmentManager}
    )

