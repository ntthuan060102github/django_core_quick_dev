from django.http import JsonResponse
from rest_framework.response import Response
import app_core.variables.response_variables as rv

class ResponseManager:
    content_type = "application/json"

    def __init__(self, data=None, status=rv.STATUS["SUCCESS"], message=rv.MESSAGES["SUCCESS"], messages={}):
        self.data = data
        self.status = status
        self.message = message
        self.messages = messages if isinstance(messages, dict) else {}

    @property
    def common(self):
        return Response(
            {
                "status": self.status,
                "message": self.message,
                "data": self.data
            },
            content_type=self.content_type
        )
    
    def standard(self, key):
        message = self.messages.get(key, rv.MESSAGES.get(key, None))
        status = rv.STATUS.get(key, self.status)
        data = self.data or key
        return Response(
            {
                "status": status,
                "message": message,
                "data": data
            },
            content_type=self.content_type
        )

    @property
    def success(self):
        self.status = rv.STATUS["SUCCESS"]
        return self.standard("SUCCESS")
    
    @property
    def validate_error(self):
        self.status = rv.STATUS["INVALID_INPUT"]
        return self.standard("INVALID_INPUT")

    @property
    def internal_server_error(self):
        self.status = rv.STATUS["INTERNAL_SERVER_ERROR"]
        return self.standard("INTERNAL_SERVER_ERROR")

    @property
    def not_found(self):
        self.status = rv.STATUS["NOT_FOUND"]
        return self.standard("NOT_FOUND")
    
    @property
    def object_not_found(self):
        self.status = rv.STATUS["OBJECT_NOT_FOUND"]
        return self.standard("OBJECT_NOT_FOUND")
