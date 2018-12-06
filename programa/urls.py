from django.urls import path
from programa.views import mostrar_programa

urlpatterns = [
	path('', mostrar_programa, name='mostrar_programa'),
]
