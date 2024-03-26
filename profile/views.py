""" view when the user is Auth."""
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from therapist.models import AppointmentManager, Therapists
from therapist.forms import UserAppointmentManager
from .models import Profile
from .forms import UserProfileForm



# Create your views here.
@login_required
def profile(request):
    """Display Profile page for the Right User"""
    queryset = AppointmentManager.objects.all()
    therapists = Therapists.objects.all()
    profile_model = get_object_or_404(Profile, user=request.user)
    form_profile = UserProfileForm(instance=request.user)

    if request.method == 'POST':
        form_profile = UserProfileForm(request.POST,
                                       request.FILES,
                                       instance=profile_model)
        if form_profile.is_valid():
            profile_model.completed_info = True
            form_profile.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                "Your profile was update successfully")
            return redirect('profile')
        else:
            messages.add_message(
                request,
                messages.WARNING,
                'Something has gone wrong check your form')
    return render(request, 'profile.html',
                  {'from_profile': form_profile,
                   'therapists': therapists,
                   'appointment_form': UserAppointmentManager,
                   'appointments': queryset})


@login_required
def delete_profile(request, user):
    """ Deletes the user's account and logs them out."""
    profile_model = get_object_or_404(Profile, user=request.user)
    
    if request.user:
        profile_model.delete()
        user.delete()
        logout(request)
        messages.add_message(
                request,
                messages.SUCCESS,
                "Your account has been successfully deleted.")
        return redirect(reverse('home'))
    else:
        messages.add_message(
                request,
                messages.WARNING,
                "Something has gone wrong.")
        return redirect(reverse('profile'))


@login_required
def edit_appointment(request, pk):
    """edit appointment view"""
    appointments = get_object_or_404(AppointmentManager, id=pk)
    print(appointments.therapist)
    if request.method == 'POST':
        appointments_form = UserAppointmentManager(request.POST, instance=appointments)
        if appointments_form.is_valid():
            
            appointments_form.save()
            return HttpResponseRedirect(reverse('profile'))

    return HttpResponseRedirect(reverse('profile'))


@login_required
def delete_appointment(request, pk):
    """
    view to delete comment
    """
    appointments = get_object_or_404(AppointmentManager, id=pk)

    if appointments.client == request.user:
        appointments.delete()
        messages.add_message(request, messages.SUCCESS, 'Appointment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'Something has gone wrong!')

    return HttpResponseRedirect(reverse('profile'))
