from rest_framework import permissions
import app_core.variables.response_variables as rv

class IsAuthenticated(permissions.BasePermission):
    message = {
        "middleware_error": "",
    }
    
    def has_permission(self, request, view):
        try:
            self.message["middleware_error"] = "TOKEN_EXPIRED"
            return True
        except Exception as e:
            raise e