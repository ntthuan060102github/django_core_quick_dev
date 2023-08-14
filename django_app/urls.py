import importlib
import pkgutil
from django.urls import path, include
from django_app.views.health import HealthView
from django_app.apps import DjangoAppConfig as AppConfigs

parent_module = __import__("django_app.routers", fromlist=[""])
package_path = parent_module.__path__[0]
child_modules = [module_name for _, module_name, _ in pkgutil.iter_modules([package_path])]

urls = []

for module in child_modules:
    urls += importlib.import_module(f"django_app.routers.{module}").urls

urlpatterns = [path(f"{AppConfigs.api_prefix}/", include(urls))]
handler404 = HealthView().not_found