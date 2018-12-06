from django.urls import path
from premios.views import entar_premios

urlpatterns = [
    path('', entar_premios, name='premios'),
]
