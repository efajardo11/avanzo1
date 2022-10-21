from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('solicitante/', views.solicitante_list),
    path('solicitantecreate/', csrf_exempt(views.solicitante_create), name='solicitanteCreate'),
]