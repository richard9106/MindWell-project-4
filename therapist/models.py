"""models to control therapist information"""
from django.contrib.auth.models import User
from django.db import models
from cloudinary.models import CloudinaryField
from django.core.exceptions import ValidationError


# Create your models here.
class Therapists(models.Model):
    """Info about Therapists"""
    TherapistId = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    specialization = models.CharField(max_length=200)
    bio = models.TextField()
    experience_years = models.PositiveIntegerField()
    location = models.CharField(max_length=200,  blank=True)
    profile_image = CloudinaryField('image', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    price = price = models.DecimalField(max_digits=8, decimal_places=2,
                                        default=0.00)
    approved = models.BooleanField(default=False)

    class Meta:
        """ order by name"""
        ordering = ["first_name"]

    def __str__(self):
        """ Show the name in the list of therapisd admin"""
        return f"{self.first_name} {self.last_name}"


HOURS_CHOICES = [
        ('09:00', '9:00 AM'),
        ('10:00', '10:00 AM'),
        ('11:00', '11:00 AM'),
        ('12:00', '12:00 PM'),
        ('13:00', '1:00 PM'),
        ('14:00', '2:00 PM'),
        ('15:00', '3:00 PM'),
        ('16:00', '4:00 PM'),
        ('17:00', '5:00 PM'),
    ]

class AppointmentManager(models.Model):
    """Model for linking user and their appointments"""
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_appointment')
    therapist = models.ForeignKey(Therapists, on_delete=models.CASCADE, related_name='therapist')
    date = models.DateField(null=True, blank=True)
    time = models.CharField(max_length=5, choices=HOURS_CHOICES)
    message = models.TextField()

    class Meta:
        """Prevent duplicate appointments with the same therapist, date, and time"""
        ordering = ["date"]
        unique_together = ['therapist', 'date', 'time']

    def __str__(self):
        """Show the appointment details"""
        return f"{self.client} has an appointment on: {self.date} at {self.time}"
    
    def clean(self):
        """
        Custom validation to prevent duplicate appointments
        """
        if AppointmentManager.objects.filter(
            therapist_id=self.therapist_id, date=self.date, time=self.time
        ).exclude(pk=self.pk).exists():
            return "This therapist already has an appointment at this date and time."
        return None
    
    def save(self, *args, **kwargs):
        # Call custom validation before saving
        error_message = self.clean()
        if error_message:
            # Handle the error message in the view
            raise ValidationError(error_message)
        super().save(*args, **kwargs)
