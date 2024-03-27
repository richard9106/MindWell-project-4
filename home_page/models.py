""" models to manage info user"""
from django.db import models


consultations_list = [
    [0, "Info"],
    [1, "Complaint"],
    [2, "Make a Suggestion"],
    [3, "Happy about the services"],

]


class ContactForm(models.Model):
    """create the model for contact form"""
    name = models.CharField(max_length=50)
    email = models.EmailField()
    consultation_type = models.IntegerField(choices=consultations_list,
                                            blank=True)
    message = models.TextField()

    def __str__(self):
        return f'{self.name} contact: {self.email}'
