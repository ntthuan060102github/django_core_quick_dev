from rest_framework.viewsets import ViewSet

from django.conf import settings as Settings
from django.db import connection

from helpers.response import ResponseManager as Response

class Health(ViewSet):
    def health(self, request):
        data = {
            "base_url": request.build_absolute_uri(),
            "main_database_host": Settings.DATABASES['default']['HOST'],
            "main_database_port": Settings.DATABASES['default']['PORT'],
            "main_database_status": connection.ensure_connection() == None,
            "cache_database_url": Settings.CACHES['default']['LOCATION'],
            # "service_name": Settings,
        }
        return Response(data).common
    
    @staticmethod
    def not_found(request, exception):
        return Response().not_found