from helpers.response import ResponseManager as Response
from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction

class CreateModelComponent():
    def create(self, request, pk=None, fields=[], excluded_fields=[], **kwargs):
        try:
            serializer = self.serializer_class(data=request.data, fields=fields, excluded=excluded_fields)
            if serializer.is_valid():
                with transaction.atomic():
                    serializer.save()
                    return Response(messages=self.messages["create"]).success
            else:
                return Response(data=serializer.errors, messages=self.messages["create"]).validate_error
        except Exception as e:
            return Response(data=str(e), messages=self.messages["create"]).internal_server_error

class RetrieveModelComponent():
    def retrieve(self, request, pk=None, fields=[], excluded_fields=[], **kwargs):
        try:
            instance = self.queryset.get(id=pk)
            serializer = self.serializer_class(
                instance, 
                excluded=excluded_fields, 
                fields=fields
            )
            return Response(data=serializer.data, messages=self.messages["retrieve"]).success
        except ObjectDoesNotExist as e:
            return Response(data=str(e), messages=self.messages["retrieve"]).object_not_found
        except Exception as e:
            return Response(data=str(e), messages=self.messages["retrieve"]).internal_server_error

class ListModelsComponent():
    def list(self, request, pk=None, fields=[], excluded_fields=[], **kwargs):
        try:
            instances = self.queryset
            serializer = self.serializer_class(
                instances, 
                exclude=excluded_fields, 
                fields=fields,
                many=True
            )
            return Response(data=serializer.data).common
        except Exception as e:
            message = kwargs.get("internal_error", str(e))
            return Response(message=message).internal_server_error
        
class UpdateModelComponent():
    def update(self, request, pk, **kwargs):
        try:
            data = request.data.copy()
            instance = self.queryset.get(id=pk)
            serializer = self.serializer_class(instance, data=data, partial=True)
            if not serializer.is_valid():
                return Response(data=serializer.errors).validate_error
            serializer.save()
            return Response().common
        except ObjectDoesNotExist as e:
            message = kwargs.get("no_data", str(e))
            return Response(message=message).object_not_found
        except Exception as e:
            message = kwargs.get("internal_error", str(e))
            return Response(message=message).internal_server_error
        
class DeleteModelComponent():
    def destroy(self, request, pk, soft_delete=True, **kwargs):
        try:
            instance = self.queryset.get(id=pk).soft_delete()
            return Response().common
        except ObjectDoesNotExist as e:
            message = kwargs.get("no_data", str(e))
            return Response(message=message).object_not_found
        except Exception as e:
            message = kwargs.get("internal_error", str(e))
            return Response(message=message).internal_server_error
