from django.core.cache import cache
from django_app.apps import DjangoAppConfig
from django_app.models.config import Config
from django_app.serializers.config_serializer import ConfigSerializer

class ConfigManager():
    def get_and_cache(self, key, timeout=24*60*60):
        try:
            value = cache.get(key=f"{DjangoAppConfig.cache_partition}:configs:{key}", default=None)

            if value is None:
                try:
                    instance = Config.objects.get(key=key)
                except Exception as e:
                    print("config does not exist!")
                
                value =  ConfigSerializer(instance).data["value"]
                cache.set(key=f"{DjangoAppConfig.cache_partition}:configs:{key}", value=value, timeout=timeout)
                
            return value
        except Exception as e:
            print(e)
            return None