import pytz
import datetime
from django.db import models, Error
from django.conf import settings as dst

class TimeStampModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, default=None)

    @classmethod
    def get_related_fields(self):
        fields = []
        for field in self._meta.get_fields():
            if models.fields.related.RelatedField.__subclasscheck__(field.__class__):
                fields.append(field.name)
        return fields

    def soft_delete(self):
        try:
            if self.deleted_at != None:
                raise Error("This object has been soft deleted")
            self.deleted_at = datetime.datetime.now(tz=dst.PY_TIME_ZONE)
            self.save(update_fields=["deleted_at"])
        except Exception as e:
            raise e

    
    