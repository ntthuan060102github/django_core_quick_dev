from rest_framework.viewsets import GenericViewSet
from rest_framework.exceptions import PermissionDenied
from django.core.exceptions import ObjectDoesNotExist
from helpers.response import ResponseManager as Response

class CommonModelViewSet(GenericViewSet):
    relation = False
    exclude_fields = []
    get_fields = []

    def retrieve(self, request, pk=None):
        try:
            instance = self.queryset.get(pk=pk)
            serializer = self.serializer_class(
                instance, 
                exclude=self.exclude_fields, 
                fields=self.get_fields
            )
            return Response(data=serializer.data).common
        except ObjectDoesNotExist as d_e:
            return Response(str(d_e)).object_not_found
        except Exception as e:
            print(e)
            return Response(str(e)).internal_server_error
    
    def create(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response().common
            else:
                return Response(data=serializer.errors).validate_error
        except Exception as e:
            print(e)
            return Response(str(e)).internal_server_error
        
    def list(self, request):
        try:
            instances = self.queryset
            serializer = self.serializer_class(
                instances, 
                exclude=self.exclude_fields, 
                fields=self.get_fields,
                many=True
            )
            return Response(data=serializer.data).common
        except ObjectDoesNotExist as d_e:
            return Response(str(d_e)).object_not_found
        except Exception as e:
            print(e)
            return Response(str(e)).internal_server_error
        
    def destroy(self, request, pk, soft_delete=True):
        try:
            instance = self.queryset.get(pk=pk).soft_delete()
            return Response().common
        except Exception as e:
            print(e)
            return Response(str(e)).internal_server_error

    def update(self, request, pk):
        try:
            data = request.data.copy()
            instance = self.queryset.get(pk=pk)
            serializer = self.serializer_class(instance, data=data, partial=True)
            if not serializer.is_valid():
                return Response(data=serializer.errors).validate_error
            serializer.save()
            return Response().common
        except ObjectDoesNotExist as d_e:
            return Response(str(d_e)).object_not_found
        except Exception as e:
            print(e)
            return Response(str(e)).internal_server_error
         
    def permission_denied(self, request, message=None, code=None):
        raise PermissionDenied(message, code)