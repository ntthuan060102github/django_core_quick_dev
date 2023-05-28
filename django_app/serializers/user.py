import re
from rest_framework import serializers
from configs.app_variables import PASSWORD_REGEX
from configs.messages import INVALID_PASSWORD
from django_app.models.user import UserModel
from django_app.serializers.base import BaseModelSerializer
from django_app.serializers.user_profile import UserProfileSerializer

class UserSerializer(BaseModelSerializer):
    class Meta:
        model = UserModel
        fields = "__all__"
        read_only_fields = ["id", "is_active", "deleted_at", "created_at", "updated_at"]

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
        regex = PASSWORD_REGEX
        if not re.search(regex, value):
            raise serializers.ValidationError(INVALID_PASSWORD)
        return value

    
    
