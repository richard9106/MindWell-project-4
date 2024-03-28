from django import forms
from .models import Profile


class UserProfileForm(forms.ModelForm):
    """Form to User profile page"""

    class Meta:
        """define the model and exclude user name"""
        model = Profile
        exclude = ('user', 'create_on', 'completed_info')

        def __init__(self, *args, **kwargs):
            """
            Add placeholders and classes, remove auto-generated
            labels
            """
            super().__init__(*args, **kwargs)
            placeholder = {
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
                if field in placeholder:
                    if self.fields[field].required:
                        placeholder = f'{placeholder[field]} *'
                    else:
                        placeholder = placeholder[field]
                    self.fields[field].widget.attrs['placeholder'] = placeholder
                if field in labels:
                    self.fields[field].label = labels[field]


