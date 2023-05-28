from rest_framework import serializers

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

    password = serializers.CharField(write_only=True, required=True)
    profile = UserProfileSerializer(required=False, many=False, default={})
    
    
