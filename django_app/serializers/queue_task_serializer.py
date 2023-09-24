from rest_framework import serializers
from django_app.models.queue_task import QueueTask

class QueueTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = QueueTask
        fields = "__all__"
        read_only_fields = ["created_at", "updated_at", "deleted_at"]
        
    eta = serializers.DateTimeField(allow_null=True, input_formats=["%Y-%m-%dT%H:%M:%S.%f%z"])
    expires = serializers.DateTimeField(allow_null=True, input_formats=["%Y-%m-%dT%H:%M:%S.%f%z"])
