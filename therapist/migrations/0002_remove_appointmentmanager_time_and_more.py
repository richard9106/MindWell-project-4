# Generated by Django 4.2.11 on 2024-03-19 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('therapist', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointmentmanager',
            name='time',
        ),
        migrations.AlterField(
            model_name='appointmentmanager',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
