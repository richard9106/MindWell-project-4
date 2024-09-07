from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Therapists
from .forms import UserAppointmentManager
from django.core.exceptions import ValidationError


@login_required
def therapilist(request):
    """View for listing therapists"""
    therapists = Therapists.objects.all()
    return render(request, "therapist_list.html", {'therapists': therapists})

@login_required
def therapist_profile(request, therapist_id):
    """Define the info to display in the therapist profile page"""
    therapist = get_object_or_404(Therapists, TherapistId=therapist_id)

    if request.method == 'POST':
        appointment_form = UserAppointmentManager(request.POST)
        if appointment_form.is_valid():
            instance = appointment_form.save(commit=False)
            instance.client = request.user
            instance.therapist = therapist
            try:
                instance.save()
                messages.add_message(request, messages.SUCCESS,"Your appointment was successfully registered.")
                return HttpResponseRedirect(reverse('therapist_profile', args=[therapist_id]))
            except ValidationError as e:
                messages.add_message(request, messages.WARNING, e.message)
        else:
            messages.add_message(request, messages.WARNING, "Please correct the errors below.")
            
 


    return render(
        request,
        "therapist_profile.html",
        {"therapist": therapist, "appointment_form": UserAppointmentManager()}
    )
    