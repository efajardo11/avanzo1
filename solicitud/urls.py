from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('solicitud/', views.solicitud_list),
    path('solicitudcreate/', csrf_exempt(views.solicitud_create), name='solicitudCreate'),
]