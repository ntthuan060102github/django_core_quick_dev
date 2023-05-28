import bcrypt
from configs.app_variables import UNICODE
from django.db import models
from django_app.models.timestamp import TimeStampModel

class UserModel(TimeStampModel):
    class Meta:
        db_table = 'user'

    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=255, unique=False, db_index=True, blank=False, null=False)
    password = models.TextField(blank=False, null=False)
    first_name = models.CharField(max_length=255, blank=False, null=False)
    middle_name = models.CharField(max_length=255, blank=True, default='')
    last_name = models.CharField(max_length=255, blank=False, null=False)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        self.password = bcrypt.hashpw(self.password.encode(UNICODE), bcrypt.gensalt())
        super(UserModel, self).save(*args, **kwargs)
        return self
    
    def check_password(self, password):
        return bcrypt.checkpw(password.encode(UNICODE), self.password.encode(UNICODE))