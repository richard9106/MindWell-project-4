# Generated by Django 4.2.11 on 2024-03-22 10:37

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profile', '0004_profile_completed_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='Therapists',
            fields=[
                ('TherapistId', models.BigAutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('specialization', models.CharField(max_length=200)),
                ('bio', models.TextField()),
                ('experience_years', models.PositiveIntegerField()),
                ('location', models.CharField(blank=True, max_length=200)),
                ('profile_image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=8)),
                ('approved', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['first_name'],
            },
        ),
        migrations.CreateModel(
            name='AppointmentManager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('message', models.TextField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userprofile', to='profile.profile')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
    ]
