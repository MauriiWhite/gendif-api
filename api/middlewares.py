import jwt

from django.db.models import Model
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer
from rest_framework.exceptions import AuthenticationFailed

from .constants import KEY, ACCESS, ALGORITH


def get_model(model: Model, id):
    try:
        return model.objects.get(pk=id)
    except model.DoesNotExist:
        raise AuthenticationFailed("User not found.")


def get_token_and_key(request):
    token = request.COOKIES.get(ACCESS)
    if not token or not KEY:
        raise AuthenticationFailed("No token")
    return token, KEY


def validate_token(request, serializer: ModelSerializer, model: Model):
    token, key = get_token_and_key(request)
    try:
        payload = jwt.decode(token, key, algorithms=[ALGORITH])
        id = payload.get("id")
    except (jwt.ExpiredSignatureError, jwt.DecodeError, AttributeError):
        raise AuthenticationFailed("Invalid token.")

    response_user = serializer(get_model(model, id)).data
    return Response(response_user)


def validate_and_return(request, serializer: ModelSerializer, model: Model):
    get_token_and_key(request)
    objects = model.objects.all()
    data = serializer(objects, many=True).data
    return Response(data)
