import os
import datetime
from celery import Celery
from django.conf import settings
from django.core.cache import cache

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_project.settings')

app = Celery('celery_worker')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.result_backend_transport_options = {
    'global_keyprefix': f"{settings.CACHE_KEY_PREFIX}:{settings.CACHE_VERSION}:celery_management:result:"
}
     
app.autodiscover_tasks()

def revoke_task(task_id, ttl=7*24*60*60):
    cache.set(f"celery_management:revoked_time:{task_id}", datetime.datetime.now(), ttl)
