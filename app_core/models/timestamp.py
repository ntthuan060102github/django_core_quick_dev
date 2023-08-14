import datetime
from django.db import models, Error
from django.db.models.query import QuerySet
from django.conf import settings as dj_set

class TimeStampManager(models.Manager):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(deleted_at=None)

class TimeStampModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, default=None)

    objects = TimeStampManager()

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
                raise Error(f"{self.__class__}: This object has been soft deleted")
            self.deleted_at = datetime.datetime.now(tz=dj_set.PY_TIME_ZONE)
            self.save(update_fields=["deleted_at"])
        except Exception as e:
            raise Exception(f"{self.__class__}: {str(e)}")
