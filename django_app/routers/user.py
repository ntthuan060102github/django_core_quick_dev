from rest_framework import routers

from django_app.views.user import UserView

router = routers.SimpleRouter(trailing_slash=False)

router.register("user", UserView, basename='user')