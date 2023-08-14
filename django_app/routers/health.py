from django.urls import path
from django_app.views.health import HealthView

urls = [
    path('health', HealthView.as_view({'get': 'health'}))
]