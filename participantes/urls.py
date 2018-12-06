from django.urls import path
from participantes.views import entrar,lista_participantes,registro_participante,editar_participante,eliminar_participante,mostrar_mapa,carga_municipio

urlpatterns = [
    path('', entrar, name='participantes'),
    path('lista', lista_participantes, name='lista_participantes'),
    path('mapa', mostrar_mapa, name='mostrar_mapa'),
    path('registrar', registro_participante, name='registro_participante'),
    path('editar/<int:id>', editar_participante, name='editar_participante'),
    path('eliminar/<int:id>', eliminar_participante, name='eliminar_participante'),
    path('carga_mun', carga_municipio, name='carga_municipio'),
]
