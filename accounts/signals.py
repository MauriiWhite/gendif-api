from django.contrib.auth.models import Group
from django.dispatch import receiver
from django.db.models.signals import post_save

from .models import Profile

NAME_DEFAULT = "Usuarios"


@receiver(post_save, sender=Profile)
def add_user_to_role(sender, instance, created, **kwargs):
    if created:
        try:
            users = Group.objects.get(name=NAME_DEFAULT)
        except Group.DoesNotExist:
            users = Group.objects.create(name=NAME_DEFAULT)

        instance.user.groups.add(users)
