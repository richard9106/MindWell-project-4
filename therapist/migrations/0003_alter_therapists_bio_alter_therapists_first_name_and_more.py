# Generated by Django 4.2.10 on 2024-03-07 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('therapist', '0002_rename_image_therapists_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='therapists',
            name='bio',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='therapists',
            name='first_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='therapists',
            name='last_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='therapists',
            name='profile_image',
            field=models.ImageField(default='profile', upload_to='static/images/t_images/'),
        ),
    ]
