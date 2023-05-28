from django_app.views.base import BaseView
from django_app.models.user import UserModel
from django_app.serializers.user import UserSerializer

class UserView(BaseView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
        


