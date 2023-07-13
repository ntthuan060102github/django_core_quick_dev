from django_app.models.user import UserModel
from django_app.serializers.user import UserSerializer
from django_app.middlewares.authentication import IsAuthenticated
from app_core.views.common_model_viewset import CommonModelViewSet
from rest_framework.decorators import action
from helpers.response import ResponseManager as Response
import random
from celery import shared_task

@shared_task
def create_user(data):
    serializer = UserSerializer(data=data)
    if not serializer.is_valid():
        return False
    serializer.save()
    return True

class UserView(CommonModelViewSet):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
    permission_classes = [IsAuthenticated]

    def random_gmail(self):
        letters = ["a", "b","c", "d","e", "f","g", "h","i", "j","k", "l","m", "n",
           "o", "p","q", "r","s", "t","u", "v","w", "x","y", "z",]
        gmail = ""
        for x in range(7):
            gmail += random.choice(letters)
        gmail += "@gmail.com"
        return gmail

    @action(methods=["GET"], detail=False)
    def queue_test(self, request):
        data = {
            "password": "Thuan123@@",
            "email": self.random_gmail(),
            "first_name": "string",
            "middle_name": "string",
            "last_name": "string",
            "gender": 0,
            "birthday": "2023-07-13",
            "phone": "string",
            "address": "string",
            "avatar": "string",
            "description": "string",
            "alternate_name": "string"
        }
        create_user.apply_async(kwargs={
            "data": data
        })
        return Response().common


    


