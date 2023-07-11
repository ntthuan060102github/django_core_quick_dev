from app_core.serializers.common_model_serializer import CommonModelSerializer

from django_app.models.user_models.user_profile import UserProfileModel

class UserProfileSerializer(CommonModelSerializer):
    class Meta:
        model = UserProfileModel
        fields = "__all__"
        read_only_fields = ["id", "created_at", "updated_at", "deleted_at", "user"]