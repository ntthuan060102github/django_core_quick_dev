from rest_framework import serializers

class BaseModelSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(required=False, read_only=True)
    updated_at = serializers.DateTimeField(required=False, read_only=True)
    
    class Meta:
        relations = {}

    def __init__(self, *args, **kwargs):
        exists = set(self.fields.keys())
        relation = kwargs.pop("relation", False)
        fields = kwargs.pop("fields", []) or exists
        exclude = kwargs.pop("exclude", [])
        
        super().__init__(*args, **kwargs)

        if relation is True:
            for r in self.Meta.relations.keys():
                self.fields[r] = self.Meta.relations[r]
            
        for field in exclude + list(exists - fields):
            self.fields.pop(field, None)

    def create(self, validated_data):
        instance = self.Meta.model.objects.create(**validated_data)
        for r in self.Meta.relations.keys():
            if r in validated_data:
                self.Meta.relations[r].create(**validated_data[r], kwargs={r: instance})

        return instance
