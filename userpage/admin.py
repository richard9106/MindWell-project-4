"""regiter the modules to admin panel"""
from django.contrib import admin
from .models import Profile


# Register your models here.
admin.site.register(Profile)
