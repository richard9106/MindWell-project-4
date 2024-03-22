# Generated by Django 4.2.11 on 2024-03-22 13:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('therapist', '0009_alter_appointmentmanager_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointmentmanager',
            name='client',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user_appointment', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
