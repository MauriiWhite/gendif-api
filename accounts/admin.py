from django.contrib import admin
from .models import GendifUser, Profile, Subgroup


class GendifUserAdmin(admin.ModelAdmin):
    list_display = ["username", "user_group", "subgroup", "date_joined"]
    list_filter = ["groups__name", "username"]

    def user_group(self, obj):
        return " - ".join([t.name for t in obj.groups.all().order_by("name")])

    user_group.short_description = "Grupo"


class ProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "user_group"]

    def user_group(self, obj):
        return " - ".join([t.name for t in obj.user.groups.all().order_by("name")])

    user_group.short_description = "Grupo"


class SubgroupAdmin(admin.ModelAdmin):
    list_display = ["name_subgroup", "created_at"]


admin.site.register(GendifUser, GendifUserAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Subgroup, SubgroupAdmin)


