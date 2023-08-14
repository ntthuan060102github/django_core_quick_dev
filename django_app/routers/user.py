from rest_framework import routers
from django_app.views.user import UserView

router = routers.SimpleRouter(False)
router.register("user", UserView, "user")
urls = router.urls