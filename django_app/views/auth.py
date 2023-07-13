from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from drf_yasg.utils import swagger_auto_schema
from django_app.validations.auth import LoginValidate
from django_app.models.user import UserModel
from helpers.response import ResponseManager as Response
from app_core.variables import response_variables as rv

class AuthenticationView(ViewSet):
    @swagger_auto_schema(method="POST", request_body=LoginValidate)
    @action(detail=False, methods=["POST"])
    def login(self, request):
        try:
            data = request.data.copy()
            validate = LoginValidate(data=data)
            if not validate.is_valid():
                return Response(validate.errors).validate_error
            validated_data = validate.validated_data
            instance = UserModel.objects.get(email=validated_data["email"])
            if instance.compare_password(validated_data["password"]):
                return Response().common
            return Response(
                status=rv.STATUS["DEFAULT"],
                message="Login failed!"
            ).common
        except UserModel.DoesNotExist:
            return Response(
                status=rv.STATUS["OBJECT_NOT_FOUND"],
                message="Email not found!"
            ).common
        except Exception as e:
            print(e)
            return Response(str(e)).internal_server_error