from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('usuario/', views.usuario_list),
    path('usuariocreate/', csrf_exempt(views.usuario_create), name='usuarioCreate'),
]