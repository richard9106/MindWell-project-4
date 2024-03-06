""" add therapist to therapist group or create group if doesn't exists"""
from django.contrib.auth.models import Group
from django.dispatch import receiver
from django.db.models.signals import post_save
from therapist.models import Therapists
from django.core.exceptions import ObjectDoesNotExist
# Create your models here.

