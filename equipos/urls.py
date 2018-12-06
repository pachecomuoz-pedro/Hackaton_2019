from django.urls import path
from equipos.views import lista_equipos,registro_equipo,editar_equipo,eliminar_equipo

urlpatterns = [
    path('', lista_equipos, name='equipos'),
    path('lista', lista_equipos, name='lista_equipos'),
    path('registrar', registro_equipo, name='registro_equipo'),
    path('editar/<int:id>', editar_equipo, name='editar_equipo'),
    path('eliminar/<int:id>', eliminar_equipo, name='eliminar_equipo'),
]
