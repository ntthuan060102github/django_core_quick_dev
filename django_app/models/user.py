from django.db import models

from django_app.models.timestamp import TimeStampModel

class UserModel(TimeStampModel):
    class Meta:
        db_table = 'user'

    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, blank=True, default='')
    last_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)