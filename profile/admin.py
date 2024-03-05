"""regiter the modules to admin panel"""
from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(SummernoteModelAdmin):
    """This code will give your admin panel greater functionality and clarity.
    We'll discuss this in more detail soon"""
    list_display = ('user', 'location', 'email')
    search_fields = ('user', 'location')
    list_filter = ('location', 'create_on')
    summernote_fields = ('description')



