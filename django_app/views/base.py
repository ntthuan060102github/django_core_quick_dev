from rest_framework.viewsets import ModelViewSet
from helpers.response import ResponseManager as Response

class BaseView(ModelViewSet):
    relation = False
    exclude_fields = []
    get_fields = []
    
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


