""" used the same model to display therapis from therapist app"""
from django import forms
from therapist.models import Therapists


class WorkWithUsForm(forms.ModelForm):
    """ Create the model for collaborateForm"""
    class Meta:
        """We select the files to apear in the form"""
        model = Therapists
        fields = (
            'name',
            'specialization',
            'experience_years',
            'location',
            'profile_picture',
            'price',
            'bio',
            )
