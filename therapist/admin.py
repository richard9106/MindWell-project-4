"""import models """

from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from .models import Therapists


@admin.register(Therapists)
class TherapistsAdmin(SummernoteModelAdmin):
    """Power Up admin """
    list_display = ('first_name', 'specialization', 'experience_years')
    search_fields = ['first_name']
    list_filter = ('experience_years',)
    prepopulated_fields = {'specialization': ('first_name',)}
    summernote_fields = ('bio',)



