from django.db import models
from app_core.models.timestamp import TimeStampModel

class UserModel(TimeStampModel):
    class Meta:
        db_table = 'users'

    class Gender(models.IntegerChoices):
        FEMALE = 0
        MALE = 1
        OTHER = 2

    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=255, unique=True, db_index=True, blank=False, null=False)
    password = models.BinaryField(blank=False, null=False)
    first_name = models.CharField(max_length=255, blank=False, null=False)
    middle_name = models.CharField(max_length=255, blank=True, default='')
    last_name = models.CharField(max_length=255, blank=False, null=False)
    gender = models.SmallIntegerField(choices=Gender.choices, default=Gender.OTHER)
    birthday = models.DateField(null=True, default=None)
    phone = models.CharField(max_length=20, null=True, default=None)
    address = models.CharField(max_length=255, null=True, default=None)
    avatar = models.CharField(max_length=255, null=True, default=None)
    description = models.TextField(null=True, default=None)
    alternate_name = models.CharField(max_length=255, null=True, default=None)
    blocked_at = models.DateTimeField(null=True, default=None)