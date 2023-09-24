from app_core.views.common_view.common_view import CommonView
from app_core.views.common_view.components import *

from django_app.models.user import UserModel
from django_app.serializers.user import UserSerializer

class UserView(
        CommonView, 
        CreateModelComponent, 
        RetrieveModelComponent, 
        ListModelsComponent, 
        UpdateModelComponent, 
        DeleteModelComponent
    ):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()