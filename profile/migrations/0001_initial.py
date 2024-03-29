# Generated by Django 4.2.10 on 2024-03-04 11:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='statics/images/profile_images/default.jpeg', upload_to='statics/images/profile_images/')),
                ('location', models.CharField(blank=True, max_length=250, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('profession', models.CharField(max_length=254)),
                ('description', models.TextField()),
                ('create_on', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
