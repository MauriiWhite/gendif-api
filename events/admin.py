from django.contrib import admin
from .models import Event, Inscriptions


class EventsAdmin(admin.ModelAdmin):
    list_display = ["id", "event_name", "created_at"]


admin.site.register(Event, EventsAdmin)
admin.site.register(Inscriptions)
