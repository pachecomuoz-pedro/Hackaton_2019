from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('participantes/', include('participantes.urls')),
    path('', include('login.urls')),
    path('equipos/', include('equipos.urls')),
    path('mentores/', include('mentores.urls')),
    path('jueces/', include('jueces.urls')),
    path('premios/', include('premios.urls')),
    path('programa/', include('programa.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
