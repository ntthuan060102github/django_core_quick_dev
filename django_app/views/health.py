from rest_framework.viewsets import ViewSet

from helpers.response import ResponseManager as Response

class Health(ViewSet):
    def health(self, request):
        return Response().common
    
    @staticmethod
    def not_found(request, exception):
        return Response().not_found