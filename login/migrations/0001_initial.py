# Generated by Django 2.1.3 on 2018-12-04 07:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(max_length=100, verbose_name='Estado')),
            ],
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('municipio', models.CharField(max_length=100, verbose_name='Municipio')),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Estado')),
            ],
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curp', models.CharField(blank=True, max_length=255)),
                ('apellido_materno', models.CharField(max_length=100, verbose_name='Apellido Materno')),
                ('telefono', models.CharField(max_length=20, verbose_name='Teléfono')),
                ('ocupacion', models.CharField(max_length=100, verbose_name='Ocupación')),
                ('foto', models.ImageField(blank=True, null=True, upload_to='participantes', verbose_name='Foto')),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Estado')),
                ('municipio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Municipio')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
