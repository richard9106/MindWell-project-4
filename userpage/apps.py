from django.apps import AppConfig


class UserpageConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'userpage'
    verbose_name = 'profiles'

    def ready(self):
        """Inicialization before app starts"""
        import userpage.signals

