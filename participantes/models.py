from django.db import models

class Estado(models.Model):
    estado = models.CharField('Estado', max_length=100)

    def __str__(self):
        return self.estado

class Municipio(models.Model):
    municipio = models.CharField('Municipio', max_length=100)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)

    def __str__(self):
        return self.municipio

class Participante(models.Model):
    curp = models.CharField('CURP', max_length=100)
    nombre = models.CharField('Nombre', max_length=100)
    apellido_paterno = models.CharField('Apellido Paterno', max_length=100)
    apellido_materno = models.CharField('Apellido Materno', max_length=100)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)
    telefono = models. CharField('Teléfono', max_length=20)
    correo = models. CharField('Correo', max_length=100)
    ocupacion = models. CharField('Ocupación', max_length=100)
    foto = models.ImageField('Foto', upload_to='participantes', null=True, blank=True)

    def __str__(self):
        return self.nombre
