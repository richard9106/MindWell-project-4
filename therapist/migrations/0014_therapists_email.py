# Generated by Django 4.2.11 on 2024-03-25 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('therapist', '0013_alter_therapists_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='therapists',
            name='email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
    ]
