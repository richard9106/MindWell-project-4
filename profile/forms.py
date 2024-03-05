from django import forms
from .models import Profile
from django.contrib.auth.models import User


class UserProfileForm(forms.ModelForm):
    """Form to User profile page"""

    class Meta:
        """define the model and exclude user name"""
        model = Profile
        exclude = ('user', 'create_on')

        def __init__(self, *args, **kwargs):
            """
            Add placeholders and classes, remove auto-generated
            labels
            """
            super().__init__(*args, **kwargs)
            placeholders = {
                'first_name': 'First Name',
                'last_name': 'Lirst Name',
                'location': 'Location',
                'email': 'Email',
                'profession': 'Profession',
                'description': 'Tel us about you'
                }

            labels = {
                'first_name': 'First Name',
                'last_name': 'Lirst Name',
                'location': 'Location',
                'email': 'Email',
                'profession': 'Profession',
                'description': 'Description'
            }

            for field in self.fields:
                if field in placeholders:
                    if self.fields[field].required:
                        placeholder = f'{placeholders[field]} *'
                    else:
                        placeholder = placeholders[field]
                    self.fields[field].widget.attrs['placeholder'] = placeholder
                if field in labels:
                    self.fields[field].label = labels[field]