from rest_framework import serializers
from .models import Event, Inscriptions
from api.gestore import set_url_img
from api.constants import DEFAULT_EVENT, DEFAULT_EVENT_URL


class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return set_url_img(
            representation, default=DEFAULT_EVENT, default_url=DEFAULT_EVENT_URL
        )


class InscriptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inscriptions
        fields = "__all__"

