from django.db import models
from participantes.models import Participante
# Create your models here.

class Vertical(models.Model):
	vertical = models.CharField('Vertical', max_length=100)

	def __str__(self):
		return self.vertical


class Equipo(models.Model):
	nombre_equipo = models.CharField('Nombre', max_length=150)
	vertical = models.ForeignKey(Vertical, on_delete=models.CASCADE)
	#m2m = models.ManyToManyField(OtherModel, related_name="%(app_label)s_%(class)s_related")
	participante_1 = models.ForeignKey(Participante,related_name='participante_1',on_delete=models.CASCADE)
	participante_2 = models.ForeignKey(Participante,related_name='participante_2',on_delete=models.CASCADE)
	participante_3 = models.ForeignKey(Participante,related_name='participante_3',on_delete=models.CASCADE)
	participante_4 = models.ForeignKey(Participante,related_name='participante_4',on_delete=models.CASCADE)

	def __str__(self):
		return self.nombre_equipo