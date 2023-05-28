from rest_framework import serializers

class BaseModelSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(required=False, read_only=True)
    updated_at = serializers.DateTimeField(required=False, read_only=True)
    
    class Options:
        relations = []

    def __init__(self, *args, **kwargs):
        exists = set(self.fields.keys())
        relation = bool(kwargs.pop("relation", True))
        fields = kwargs.pop("fields", []) or exists
        exclude = kwargs.pop("exclude", [])
        
        super().__init__(*args, **kwargs)

        if relation is False:
            for r in self.Options.relations:
                self.fields.pop(r, None)
            
        for field in exclude + list(exists - fields):
            self.fields.pop(field, None)

    def create(self, validated_data):
        instance = self.Meta.model.objects.create(**validated_data)
        for r in self.Meta.relations.keys():
            if r in validated_data:
                self.Meta.relations[r].create(**validated_data[r], kwargs={r: instance})

        return instance
