from django.db import models

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
    
    