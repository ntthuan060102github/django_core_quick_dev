from rest_framework_nested import routers
from django_app.views.auth import AuthenticationView

router = routers.SimpleRouter(trailing_slash=False)
router.register("auth", AuthenticationView, basename='auth')

urls = router.urls
