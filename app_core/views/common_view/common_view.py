from rest_framework.viewsets import GenericViewSet
from rest_framework.exceptions import PermissionDenied

class CommonView(GenericViewSet):
    relation = False
    messages = None

    def permission_denied(self, request, message=None, code=None):
        raise PermissionDenied(message, code)
