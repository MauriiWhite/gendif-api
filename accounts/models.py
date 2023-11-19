from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser
from api.constants import DEFAULT_PROFILE, DEFAULT_SUBGROUP


class Subgroup(models.Model):
    name_subgroup = models.CharField(
        verbose_name="Nombre del Subgrupo",
        max_length=150,
        unique=True,
        help_text="Este campo puede poseer cualquier tipo de valor alfanumérico",
    )

    created_at = models.DateTimeField(
        verbose_name="Fecha de creación",
        editable=False,
        help_text="Por defecto es la fecha y hora actual",
        default=timezone.now,
    )

    image = models.TextField(
        verbose_name="Imagen del Subgrupo",
        blank=True,
        default=DEFAULT_SUBGROUP,
    )

    class Meta:
        verbose_name = "Subgrupo"
        verbose_name_plural = "Subgrupos"

    def __str__(self) -> str:
        return f"{self.pk} | {self.name_subgroup}"


class GendifUser(AbstractUser):
    last_name = models.CharField(verbose_name="Apellido", max_length=150, blank=True)

    middle_name = models.CharField(
        verbose_name="Segundo Apellido", max_length=150, blank=True
    )
    subgroup = models.ForeignKey(
        Subgroup,
        verbose_name="Subgrupo",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text="Subgrupo al que pertenece",
    )

    date_joined = models.DateTimeField(
        verbose_name="Creación de la cuenta", editable=False, auto_now_add=True
    )

    class Meta:
        verbose_name = "usuario"
        verbose_name_plural = "usuarios"

    def __str__(self) -> str:
        return f"{self.pk} | {self.username}"


class Profile(models.Model):
    user = models.OneToOneField(
        GendifUser,
        on_delete=models.CASCADE,
        related_name="profile",
        verbose_name="Usuario",
        primary_key=True,
    )

    image = models.TextField(
        verbose_name="Imagen de perfil", blank=True, default=DEFAULT_PROFILE
    )

    class Meta:
        verbose_name = "perfil"
        verbose_name_plural = "perfiles"

    def __str__(self) -> str:
        return self.user.username


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


post_save.connect(create_user_profile, sender=GendifUser)
post_save.connect(save_user_profile, sender=GendifUser)
