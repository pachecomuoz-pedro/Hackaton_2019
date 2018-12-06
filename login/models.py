from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from participantes.models import Estado, Municipio


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    curp = models.CharField(max_length=50, blank=True)
    nombre = models.CharField(max_length=30, blank=True)
    apellido_paterno = models.CharField(max_length=30, blank=True)
    apellido_materno = models.CharField(max_length=30, blank=True)
    estado = models.ForeignKey(Estado, related_name='estado_user',on_delete=models.CASCADE, null=True)
    municipio = models.ForeignKey(Municipio, related_name='municipio_user',on_delete=models.CASCADE, null=True)
    telefono = models.CharField(max_length=20, blank=True)
    email = models.EmailField(max_length=254, blank=True)
    ocupacion = models.CharField(max_length=100, blank=True)
    foto = models.ImageField(upload_to='participantes', null=True, blank=True)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
