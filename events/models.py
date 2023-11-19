from django.db import models
from django.core.exceptions import ValidationError

from accounts.models import GendifUser
from api.constants import DEFAULT_EVENT


class Event(models.Model):
    event_name = models.CharField(
        verbose_name="Nombre del Evento",
        max_length=50,
        help_text="Este campo puede poseer cualquier tipo de valor alfanumérico",
    )

    description = models.TextField(
        verbose_name="Descripción",
        max_length=500,
    )

    start = models.DateTimeField(verbose_name="Fecha de Inicio")
    finish = models.DateTimeField(verbose_name="Fecha de Fin")

    image = models.TextField(
        verbose_name="Imagen del Evento",
        blank=True,
        default=DEFAULT_EVENT,
    )

    created_at = models.DateTimeField(
        verbose_name="Fecha de creación",
        editable=False,
        help_text="Por defecto es la fecha y hora actual",
        auto_now_add=True,
    )

    def clean(self):
        if self.start and not self.finish:
            raise ValidationError(
                "Debes proporcionar una fecha de terminación para el evento."
            )

    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"

    def __str__(self) -> str:
        return f"{self.pk} | {self.event_name}"


class Inscriptions(models.Model):
    user_id = models.ForeignKey(
        GendifUser,
        verbose_name="Id de Usuario",
        on_delete=models.CASCADE,
    )

    event_id = models.ForeignKey(
        Event, verbose_name="Id de Evento", on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "Inscripción"
        verbose_name_plural = "Inscripciones"

    def __str__(self) -> str:
        return f"{self.user_id} | {self.event_id}"
