from django.db import models

from django_app.models.timestamp import TimeStampModel

class UserModel(TimeStampModel):
    class Meta:
        db_table = 'user'

    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=255, unique=True, db_index=True, blank=False, null=False)
    password = models.CharField(max_length=255, blank=False, null=False)
    first_name = models.CharField(max_length=255, blank=False, null=False)
    middle_name = models.CharField(max_length=255, blank=True, default='')
    last_name = models.CharField(max_length=255, blank=False, null=False)
    is_active = models.BooleanField(default=True)