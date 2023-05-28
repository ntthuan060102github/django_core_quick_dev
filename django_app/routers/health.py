from django.urls import path
from django_app.views.health import Health

urls = [
    path('health', Health.as_view({'get': 'health'}))
]