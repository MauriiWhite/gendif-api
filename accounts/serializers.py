from rest_framework import serializers

from .models import GendifUser, Subgroup, Profile
from api.gestore import set_url_img
from api.constants import (
    DEFAULT_PROFILE,
    DEFAULT_PROFILE_URL,
    DEFAULT_SUBGROUP,
    DEFAULT_SUBGROUP_URL,
)


class GendifUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, style={"input_type": "password"}
    )

    class Meta:
        model = GendifUser
        fields = (
            "id",
            "username",
            "password",
            "date_joined",
            "is_staff",
            "first_name",
            "last_name",
            "middle_name",
            "subgroup",
            "groups",
        )
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return set_url_img(
            representation, default=DEFAULT_PROFILE, default_url=DEFAULT_PROFILE_URL
        )


class SubgroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subgroup
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return set_url_img(
            representation, default=DEFAULT_SUBGROUP, default_url=DEFAULT_SUBGROUP_URL
        )
