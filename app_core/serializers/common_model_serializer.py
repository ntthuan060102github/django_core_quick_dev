from rest_framework import serializers

class CommonModelSerializer(serializers.ModelSerializer):
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
        

        self.__verify_option_referenced_by()
        self.__verify_content_referenced_by()
        
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
    
    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

    def __verify_option_referenced_by(self):
        if hasattr(self.Options, "referenced_by"):
            referenced_by = getattr(self.Options, "referenced_by", None)
            if (
                not isinstance(referenced_by, list) 
                or (
                    any(
                        map(lambda x: not isinstance(x, str), referenced_by)
                    )
                    and referenced_by != []
                )
            ):
                exc_obj = f"{self.__class__.__name__}.Options.referenced_by"
                raise Exception(f"{exc_obj} should be a list of strings.")
            
    def __verify_content_referenced_by(self):
        related_fiels = self.Meta.model.get_related_fields()
        # print("---------------------------------------------------")
        # print(self.Meta.model)
        # print(self.fields)