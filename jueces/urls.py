from django.urls import path
from jueces.views import entar_jueces

urlpatterns = [
    path('', entar_jueces, name='jueces'),
]
