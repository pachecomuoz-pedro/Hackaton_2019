from django.urls import path
from login.views import login_inicio, login_hackaton ,logout_hackaton, registrar_participante


urlpatterns = [
    path('', login_inicio, name='login'),
    path('entrar', login_hackaton, name='login_hackaton'),
    path('salir', logout_hackaton, name='logout_hackaton'),
    path('registrar', registrar_participante, name='registrar_participante'),
]


#from django.conf.urls import url, include
#from django.contrib.auth import views as auth_views

#from login import views as core_views


#urlpatterns = [
#    url(r'^$', core_views.login_inicio, name='login'),
#    url(r'^entrar/$', auth_views.LoginView.as_view(template_name="login.html"), name='login_inicio'),
#    url(r'^salir/$', auth_views.LogoutView.as_view(next_page='login'), name='logout_hackaton'),
#    url(r'^registrar/$', core_views.login_hackaton, name='signup'),
#]
