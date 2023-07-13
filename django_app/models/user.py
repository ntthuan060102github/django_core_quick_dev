import bcrypt
import django_app.app_configs.app_variables as av
from django.db import models
from django_app.models.timestamp import TimeStampModel

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

    def save(self, *args, **kwargs):
        if self.id is None or kwargs.get("password_update", False) == True:
            self.password = bcrypt.hashpw(self.password.encode(av.UNICODE), bcrypt.gensalt())
        super(UserModel, self).save(*args, **kwargs)
        return self

    def update_password(self, password):
        self.password = bcrypt.hashpw(password.encode(av.UNICODE), bcrypt.gensalt())
        self.save(password_update=True)
        return self.compare_password(password)

    def compare_password(self, password: str):
        return bcrypt.checkpw(password.encode(av.UNICODE), self.password)
    