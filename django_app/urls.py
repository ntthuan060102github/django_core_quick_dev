from django.conf.urls import handler404

from django_app.views.health import Health

from django_app.routers.user import router as user_router
from django_app.routers.swagger import urls as swagger_router
from django_app.routers.health import urls as health_router

urlpatterns = swagger_router + user_router.urls + health_router

handler404 = Health().not_found