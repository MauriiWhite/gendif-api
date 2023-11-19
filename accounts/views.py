from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from rest_framework.exceptions import AuthenticationFailed

from api.tokens import generate_token
from api.gestore import delete_resource, resource_update
from api.constants import ACCESS, DEFAULT_PROFILE, DEFAULT_SUBGROUP

from .models import GendifUser, Subgroup, Profile
from .serializers import GendifUserSerializer, SubgroupSerializer, ProfileSerializer
from api.middlewares import (
    validate_token,
    validate_and_return,
    get_token_and_key,
)


class RegisterView(APIView):
    def post(self, request):
        serializer = GendifUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return LoginView().post(request)


class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        if not (username and password):
            raise AuthenticationFailed("Invalid username or password.")

        user = GendifUser.objects.filter(username=username).first()

        if not user or not user.check_password(password):
            raise AuthenticationFailed("Invalid username or password.")

        token = generate_token(user)
        response = Response(data={ACCESS: token})
        response.set_cookie(
            key=ACCESS, value=token, httponly=True, samesite="Lax", secure=True
        )
        return response


class UserView(APIView):
    def get(self, request):
        return validate_token(request, GendifUserSerializer, GendifUser)


class ProfileView(APIView):
    parser_classes = [MultiPartParser]

    def get(self, request):
        return validate_token(request, ProfileSerializer, Profile)

    def put(self, request):
        get_token_and_key(request)
        return resource_update(request, Profile, "user", "users")

    def delete(self, request):
        get_token_and_key(request)
        return delete_resource(request, Profile, "user", DEFAULT_PROFILE)


class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie(ACCESS, samesite="Lax")
        response.data = {"msg": "success"}
        return response


class SubgroupView(APIView):
    def get(self, request):
        return validate_and_return(request, SubgroupSerializer, Subgroup)

    def put(self, request):
        get_token_and_key(request)
        return resource_update(request, Subgroup, "subgroup", "subgroups")

    def delete(self, request):
        get_token_and_key(request)
        return delete_resource(request, Subgroup, "subgroup", DEFAULT_SUBGROUP)
