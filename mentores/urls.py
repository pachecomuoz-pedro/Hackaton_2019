from django.urls import path
from mentores.views import entar_mentores

urlpatterns = [
    path('', entar_mentores, name='mentores'),
]
