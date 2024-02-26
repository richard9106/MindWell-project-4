# Generated by Django 4.2.10 on 2024-02-26 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('therapist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='therapists',
            name='name',
            field=models.CharField(default='my name', max_length=255),
        ),
        migrations.AlterField(
            model_name='therapists',
            name='location',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='therapists',
            name='profile_picture',
            field=models.ImageField(blank=True, upload_to='static/images/therapist_profile_pics/'),
        ),
    ]
