# Generated by Django 4.2.10 on 2024-03-07 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('therapist', '0004_alter_therapists_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='therapists',
            name='profile_image',
            field=models.ImageField(default='default.jpg', upload_to='t_images/'),
        ),
    ]
