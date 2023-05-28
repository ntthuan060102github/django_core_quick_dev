from rest_framework import serializers

class BaseModelSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(required=False, read_only=True)
    updated_at = serializers.DateTimeField(required=False, read_only=True)
    
    class Options:
        referenced_by = []

    def __init__(self, *args, **kwargs):
        exists = set(self.fields.keys())
        relation = bool(kwargs.pop("relation", True))
        fields = kwargs.pop("fields", []) or exists
        exclude = kwargs.pop("exclude", [])
        
        super().__init__(*args, **kwargs)

        if relation is False:
            for r in self.Options.referenced_by:
                self.fields.pop(r, None)
            
        for field in exclude + list(exists - fields):
            self.fields.pop(field, None)

    def create(self, validated_data):
        referenced_by = {
            r: validated_data.pop(r) for r in self.Options.referenced_by if r in validated_data
        }
        instance = self.Meta.model.objects.create(**validated_data)
        for k, v in referenced_by.items():
            related_fields = self.fields[k].__class__.Meta.model.get_related_fields()
            new_v = {
                **v,
                **{rf: instance for rf in related_fields}
            }
            self.fields[k].__class__.Meta.model.objects.create(**new_v)
        
        return instance
