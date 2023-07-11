from django_app.middlewares.authentication import IsAuthenticated
from app_core.views.common_model_viewset import CommonModelViewSet
from django_app.models.user_models.user import UserModel
from django_app.serializers.user import UserSerializer
from rest_framework.decorators import action
from helpers.response import ResponseManager as Response

class UserView(CommonModelViewSet):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=["POST"])
    def login(self, request):
        return Response().common
    


