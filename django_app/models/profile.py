from django.db import models

from django_app.models.timestamp import TimeStampModel
from django_app.models.user import UserModel

class UserProfileModel(TimeStampModel):
    class Meta:
        db_table = 'user_profile'

    class Gender(models.IntegerChoices):
        FEMALE = 0
        MALE = 1
        OTHER = 2

    id = models.AutoField(primary_key=True)
    gender = models.SmallIntegerField(choices=Gender.choices, default=2)
    birthday = models.DateField(null=True, default=None)
    phone = models.CharField(max_length=20, null=True, default=None)
    address = models.CharField(max_length=255, null=True, default=None)
    avatar = models.CharField(max_length=255, null=True, default=None)
    descrtion = models.TextField(null=True, default=None)
    alternate_name = models.CharField(max_length=255, null=True, default=None)
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='profile')