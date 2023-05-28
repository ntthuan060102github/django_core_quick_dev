from rest_framework import routers

from django_app.views.user import UserView\

router = routers.SimpleRouter()

router.register("user", UserView, basename='user')