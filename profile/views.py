""" view when the user is Auth."""
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth import logout
from .models import Profile
from .forms import UserProfileForm


# Create your views here.
@login_required
def profile(request):
    """Display Profile page for the Right User"""
    profile_model = get_object_or_404(Profile, user=request.user)
    form_profile = UserProfileForm(instance=request.user)

    if request.method == 'POST':
        form_profile = UserProfileForm(request.POST, request.FILES, instance=profile_model)
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
    return render(request, 'profile.html', {'from_profile': form_profile})


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
def my_appointments(request):
    """appointments view"""
    return render(request, 'my_appointments.html')