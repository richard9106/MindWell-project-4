"""import models """

from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from .models import Therapists, AppointmentManager


@admin.register(Therapists)
class TherapistsAdmin(SummernoteModelAdmin):
    """display therapist admin """
    list_display = ('first_name', 'specialization', 'experience_years')
    search_fields = ['first_name']
    list_filter = ('experience_years',)
    prepopulated_fields = {'specialization': ('first_name',)}
    summernote_fields = ('bio',)


@admin.register(AppointmentManager)
class AppointmentManagerAdmin(SummernoteModelAdmin):
    """manage appointments admin view"""
    list_display = ('client', 'date', 'message')
    search_fields = ['date']
    summernote_fields = ('message',)
