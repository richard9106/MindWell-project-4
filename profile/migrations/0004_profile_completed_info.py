# Generated by Django 4.2.11 on 2024-03-21 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0003_profile_first_name_profile_last_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='completed_info',
            field=models.BooleanField(default=False),
        ),
    ]
