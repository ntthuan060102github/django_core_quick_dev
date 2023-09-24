import json
import datetime
from django.core.cache import cache
from celery.signals import after_task_publish, task_postrun, task_prerun, worker_ready, task_revoked
from app_core.celery import app
from django_app.models.queue_task import QueueTask
from django_app.serializers.queue_task_serializer import QueueTaskSerializer

@after_task_publish.connect
def _task_sent_handler(sender=None, headers=None, body=None, **kwargs):
    try:
        task_id = headers["id"]
        task_info = {
            "id": task_id,
            "task": sender,
            "eta": headers["eta"],
            "expires": headers["expires"],
            "retries": headers["retries"],
            "kwargs": headers["kwargsrepr"]
        }
        serializer = QueueTaskSerializer(data=task_info)

        if not serializer.is_valid():
            print("after_task_publish@validate:", serializer.errors)
        else:
            serializer.save()
    except Exception as exc:
        print("after_task_publish: ", exc)
        
@task_prerun.connect
def _task_pre_execute(task_id, **kwargs):
    try:
        instance = QueueTask.objects.get(id=task_id)
        serializer = QueueTaskSerializer(
            instance=instance, 
            data={
                "status": "STARTED",
                "started_at": datetime.datetime.now()
            }, 
            partial=True
        )
        
        if not serializer.is_valid():
            print(serializer.errors)
        else:
            serializer.save()
        
        if cache.get(f"celery_management:revoked_time:{task_id}", False):
            app.control.revoke(task_id, terminate=True, signal='SIGKILL')
            cache.delete(f"celery_management:revoked_time:{task_id}")
            
    except Exception as exc:
        print("task_prerun: ", exc)
        
@task_postrun.connect
def _task_executed(task_id, retval, state, **kwargs):
    try:
        instance = QueueTask.objects.get(id=task_id)
        serializer = QueueTaskSerializer(
            instance=instance, 
            data={
                "result": str(retval), 
                "status": state,
                "done_at": datetime.datetime.now()
            }, 
            partial=True
        )
        
        if not serializer.is_valid():
            print(serializer.errors)
        else:
            serializer.save()
            
    except Exception as exc:
        print("task_postrun@exc: ", exc)
        
@task_revoked.connect
def _task_revoked(request, terminated, signum, expired, **kwargs):
    try:
        if terminated:
            instance = QueueTask.objects.get(id=request.id)
            serializer = QueueTaskSerializer(
                instance=instance, 
                data={
                    "status": "EXPIRED" if expired else "REVOKED",
                    "revoked_at": datetime.datetime.now()
                }, 
                partial=True
            )
            
            if not serializer.is_valid():
                print(serializer.errors)
            else:
                serializer.save()
    except Exception as exc:
        print("task_revoked@exc: ", exc)
            
@worker_ready.connect
def _worker_ready(**kwargs):
    return kwargs
