import re
from rest_framework import serializers
from django_app.models.user import UserModel
from app_core.serializers.common_model_serializer import CommonModelSerializer

class UserSerializer(CommonModelSerializer):
    class Meta:
        model = UserModel
        fields = "__all__"
        read_only_fields = ["id", "is_active", "created_at", "updated_at", "deleted_at", "blocked_at"]

    class Options:
        referenced_by = ["profile"]