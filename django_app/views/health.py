from django.db import connection
from django.conf import settings
from django_redis import get_redis_connection
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from helpers.response import ResponseManager as Response

class HealthView(ViewSet):
    def health(self, request):
        data = {
            "base_url": request.build_absolute_uri(),
            "main_database": self.__get_main_database_connection_info(),
            "cache_database": self.__get_redis_connection_info(),
            "environment": settings.ENVIRONMENT,
            "debug": settings.DEBUG
        }
        return Response(data).common
    
    def __get_redis_connection_info(self):
        try:
            redis_connection = get_redis_connection("default")
            conn_inf = {
                "status": redis_connection.ping()
            }
            if settings.ENVIRONMENT != "production":
                conn_kwagrs = redis_connection.connection_pool.connection_kwargs
                conn_inf = {
                    **conn_inf,
                    **{
                        "host": conn_kwagrs['host'],
                        "port": conn_kwagrs['port'],
                        "database": conn_kwagrs['db']
                    }
                }
            return conn_inf
        except Exception as e:
            return {
                "status": False,
                "error": str(e)
            }
        
    def __get_main_database_connection_info(self):
        try:
            main_database_connection = connection
            return {
                "status": main_database_connection.ensure_connection() == None
            }
        except Exception as e:
            return {
                "status": False,
                "error": str(e)
            }

    @staticmethod
    def not_found(request, exception):
        return Response().not_found