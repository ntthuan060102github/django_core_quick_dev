from django.urls import re_path

from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
   openapi.Info(
      title="API DOCUMENTATION",
      default_version="release",
      description="API DOCUMENTATION",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="ntthuan060102.work@gmail.com"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urls = [
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]