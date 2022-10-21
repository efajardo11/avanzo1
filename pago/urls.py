from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('pago/', views.pago_list),
    path('pagocreate/', csrf_exempt(views.pago_create), name='pagoCreate'),
]