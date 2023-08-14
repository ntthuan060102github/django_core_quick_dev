from rest_framework import serializers

class CommonModelSerializer(serializers.ModelSerializer):
    class Options:
        nested_serializers = []

    def __init__(self, *args, **kwargs):
        existing = set(self.fields.keys())
        relation = bool(kwargs.pop("relation", True))
        allowed = kwargs.pop("fields", []) or existing
        excluded = kwargs.pop("excluded", [])
        
        super().__init__(*args, **kwargs)
        
        self.__verify_option_nested_serializers()
        # self.__verify_content_nested_serializers()
        
        if relation is False:
            for r in self.Options.nested_serializers:
                self.fields.pop(r, None)
            
        for field in excluded + list(existing - allowed):
            self.fields.pop(field, None)

    def create(self, validated_data):
        nested_serializers = {
            r: validated_data.pop(r) for r in self.Options.nested_serializers if r in validated_data
        }
        instance = self.Meta.model.objects.create(**validated_data)
        
        for key, value in nested_serializers.items():
            if isinstance(self.fields[key], serializers.ListSerializer):
                related_serializer_instance = self.fields[key].child
            else:
                related_serializer_instance = self.fields[key]
            self.__create_nested_instances(
                instance, 
                related_serializer_instance, 
                value
            )
            
        return instance
    
    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

    def __verify_option_nested_serializers(self):
        if hasattr(self.Options, "nested_serializers"):
            nested_serializers = getattr(self.Options, "nested_serializers", None)
            if (
                not isinstance(nested_serializers, list) 
                or (
                    any(
                        map(lambda x: not isinstance(x, str), nested_serializers)
                    )
                    and nested_serializers != []
                )
            ):
                exc_obj = f"{self.__class__.__name__}.Options.nested_serializers"
                raise Exception(f"{exc_obj} should be a list of strings.")
            
    def __verify_content_nested_serializers(self):
        related_fiels = self.Meta.model.get_related_fields()
        # print("---------------------------------------------------")
        # print(self.Meta.model)
        # print(self.fields)

    def __create_nested_instances(self, referenced_instance, serializer_instance, dataset):
        model = serializer_instance.Meta.model
        related_model_fields = model.get_related_fields()

        if not isinstance(dataset, list):
            dataset = [dataset]

        for data in dataset:
            nested_serializers = {
                r: data.pop(r) 
                for r in serializer_instance.Options.nested_serializers 
                if r in data
            }
            instance = model.objects.create(
                **{
                    **data, 
                    related_model_fields[0]: referenced_instance
                }
            )
            for nested_serializer_key in nested_serializers.keys():
                nested_serializer_field = serializer_instance.fields.get(nested_serializer_key)
                nested_serializer_instance = getattr(
                    nested_serializer_field, 
                    "child", 
                    nested_serializer_field
                )
                self.__create_nested_instances(
                    instance, 
                    nested_serializer_instance, 
                    nested_serializers[nested_serializer_key]
                )
