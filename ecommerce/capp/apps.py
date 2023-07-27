

from django.apps import AppConfig

class cappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'capp'

    def ready(self):
        import capp.permissions
