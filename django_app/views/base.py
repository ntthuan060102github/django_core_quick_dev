from rest_framework.viewsets import ModelViewSet
from django.core.exceptions import ObjectDoesNotExist
from helpers.response import ResponseManager as Response

class BaseView(ModelViewSet):
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
    



