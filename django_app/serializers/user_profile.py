from django_app.serializers.base import BaseModelSerializer

from django_app.models.user_models.user_profile import UserProfileModel

class UserProfileSerializer(BaseModelSerializer):
    class Meta:
        model = UserProfileModel
        fields = "__all__"
        read_only_fields = ["id", "created_at", "updated_at", "deleted_at", "user"]