import app_core.variables.response_variables as rv
from django.http import JsonResponse

class RefactorResponse:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            response = self.get_response(request)
            
            if "middleware_error" in response.data:
                error_code = str(response.data["middleware_error"])
                response.data = {
                    "data": None,
                    "status": rv.STATUS[error_code],
                    "message": rv.MESSAGES[error_code]
                }
                return JsonResponse(response.data)
            return response
        except Exception as e:
            return JsonResponse({
                "data": str(e),
                "status": rv.STATUS["INTERNAL_SERVER_ERROR"],
                "message": rv.MESSAGES["INTERNAL_SERVER_ERROR"]
            })