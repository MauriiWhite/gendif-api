from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView
from rest_framework.exceptions import NotAcceptable, NotAuthenticated
from rest_framework.response import Response

from accounts.models import GendifUser
from .models import Event, Inscriptions
from .serializers import EventsSerializer
from api.constants import DEFAULT_EVENT
from api.gestore import resource_update, delete_resource
from api.middlewares import validate_and_return, get_token_and_key


class EventsView(APIView):
    def get(self, request):
        return validate_and_return(request, EventsSerializer, Event)

    def post(self, request):
        get_token_and_key(request)

        username = request.data.get("username")
        first_name = request.data.get("first_name")
        last_name = request.data.get("last_name")
        middle_name = request.data.get("middle_name")
        event_id = request.data.get("event_id")

        if not (username and first_name and last_name and middle_name and event_id):
            raise NotAcceptable("Insufficient user information.")

        try:
            user = GendifUser.objects.get(username=username)
        except ObjectDoesNotExist:
            raise NotAuthenticated("User not authenticated.")

        if not user.first_name or not user.last_name or not user.middle_name:
            user.first_name = first_name
            user.last_name = last_name
            user.middle_name = middle_name
            user.save()

        user_event = Inscriptions.objects.filter(
            event_id=event_id, user_id=user.pk
        ).first()
        if user_event:
            raise NotAcceptable("User already registered.")

        event = Event.objects.get(pk=event_id)
        Inscriptions.objects.create(event_id=event, user_id=user)

        return Response({"msg": "Registration done."})

    def put(self, request):
        get_token_and_key(request)
        return resource_update(request, Event, "event", "events")

    def delete(self, request):
        get_token_and_key(request)
        return delete_resource(request, Event, "event", DEFAULT_EVENT)
