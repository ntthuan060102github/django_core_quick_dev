from app_core.serializers.common_model_serializer import CommonModelSerializer
from django_app.models.config import Config

class ConfigSerializer(CommonModelSerializer):
    class Meta:
        model = Config
        fields = "__all__"