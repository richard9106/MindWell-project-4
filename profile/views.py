""" view when the user is Auth."""
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from .models import Profile
from django.contrib.auth import logout
from .forms import UserProfileForm


# Create your views here.
@login_required
def profile(request):
    """Display Profile page for the Right User"""
    profile_model = get_object_or_404(Profile, user=request.user)
    form_profile = UserProfileForm(instance=request.user)

    if request.method == 'POST':
        form_profile = UserProfileForm(request.POST, instance=profile_model)
        if form_profile.is_valid():
            form_profile.save()
            messages.success(request, 'Your profile was update successfully')
            return redirect('profile')
        else:
            messages.error(request, 'Something has gone wrong check your form')
    return render(request, 'profile.html', {'from_profile': form_profile})


@login_required
def delete_profile(request):
    """ Deletes the user's account and logs them out."""
    if request.method == 'POST':
        user = request.user
        user.delete()
        logout(request)
        messages.success(
            request, 'Your account has been successfully deleted.')
        return redirect(reverse('home'))
    else:
        return redirect(reverse('profile'))
