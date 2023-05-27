from django_app.serializers.base import BaseModelSerializer

from django_app.models.profile import UserProfileModel

class UserProfileSerializer(BaseModelSerializer):
    class Meta:
        model = UserProfileModel
        fields = "__all__"