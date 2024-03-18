"""regiter the modules to admin panel"""
from django.contrib import admin
from .models import ContactForm


admin.site.register(ContactForm)


