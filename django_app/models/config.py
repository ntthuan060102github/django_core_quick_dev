from django.db import models
from app_core.models.timestamp import TimeStampModel

class Config(TimeStampModel):
    class Meta:
        db_table = "mypt_configs"
        
    id = models.AutoField(primary_key=True)
    key = models.CharField(max_length=100, unique=True, blank=False, null=False)
    value = models.JSONField(blank=False, null=False)
    description_vi = models.TextField(blank=True, null=False, default="")
    description_en = models.TextField(blank=True, null=False, default="")
