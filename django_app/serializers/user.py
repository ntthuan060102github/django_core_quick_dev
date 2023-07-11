import re
from rest_framework import serializers
import django_app.app_configs.app_messages as amsg
import django_app.app_configs.app_variables as av
from django_app.models.user_models.user import UserModel
from app_core.serializers.common_model_serializer import CommonModelSerializer
from django_app.serializers.user_profile import UserProfileSerializer

class UserSerializer(CommonModelSerializer):
    class Meta:
        model = UserModel
        fields = "__all__"
        read_only_fields = ["id", "is_active", "created_at", "updated_at", "deleted_at"]

    class Options:
        referenced_by = ["profile"]

    password = serializers.CharField(
        write_only=True, 
        required=True, 
        min_length=8, 
        max_length=20
    )
    profile = UserProfileSerializer(required=False, many=False, default={})

    def validate_password(self, value):
        regex = av.PASSWORD_REGEX
        if not re.search(regex, value):
            raise serializers.ValidationError(amsg.INVALID_PASSWORD)
        return value

    
    
