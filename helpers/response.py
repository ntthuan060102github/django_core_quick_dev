from django.http import JsonResponse
from rest_framework.response import Response
from configs.response_variables import STATUS, MESSAGES

class ResponseManager:
    def __init__(self, data=None, status=STATUS["SUCCESS"], message=MESSAGES["SUCCESS"]):
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
                "status": STATUS["INVALID_INPUT"],
                "message": MESSAGES["INVALID_INPUT"],
                "data": self.data
            }
        )

    @property
    def internal_server_error(self):
        return Response(
            {
                "status": STATUS["INTERNAL_SERVER_ERROR"],
                "message": MESSAGES["INTERNAL_SERVER_ERROR"],
                "data": self.data
            }
        )

    @property
    def not_found(self):
        return JsonResponse(
            {
                "status": STATUS["NOT_FOUND"],
                "message": MESSAGES["NOT_FOUND"],
                "data": None
            }
        )