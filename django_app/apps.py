from django.apps import AppConfig

class DjangoAppConfig(AppConfig):
    name = 'django_app'
    default_auto_field = 'django.db.models.BigAutoField'
    service_name_abbreviation = "django-core"
    service_name_semantic = "Django Core"
    service_version = "1.0.0"
    service_version_abbreviation = "v1"
    api_prefix = f"{service_name_abbreviation}/{service_version_abbreviation}"

    def ready(self):
        import django_app._celery_signal_handler
