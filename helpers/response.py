from django.http import JsonResponse
from rest_framework.response import Response
import configs.response_variables as rv

class ResponseManager:
    def __init__(self, data=None, status=rv.STATUS["SUCCESS"], message=rv.MESSAGES["SUCCESS"]):
        self.data = data
        self.status = status
        self.message = message

    @property
    def common(self):
        return Response(
            {
                "status": self.status,
                "message": self.message,
                "data": self.data
            }
        )
    
    @property
    def validate_error(self):
        return Response(
            {
                "status": rv.STATUS["INVALID_INPUT"],
                "message": rv.MESSAGES["INVALID_INPUT"],
                "data": self.data
            }
        )

    @property
    def internal_server_error(self):
        return Response(
            {
                "status": rv.STATUS["INTERNAL_SERVER_ERROR"],
                "message": rv.MESSAGES["INTERNAL_SERVER_ERROR"],
                "data": self.data
            }
        )

    @property
    def not_found(self):
        return JsonResponse(
            {
                "status": rv.STATUS["NOT_FOUND"],
                "message": rv.MESSAGES["NOT_FOUND"]
            }
        )
    
    @property
    def object_not_found(self):
        return JsonResponse(
            {
                "data": self.data,
                "status": rv.STATUS["OBJECT_NOT_FOUND"],
                "message": rv.MESSAGES["OBJECT_NOT_FOUND"]
            }
        )