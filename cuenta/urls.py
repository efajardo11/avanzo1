from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('cuenta/', views.cuenta_list),
    path('cuentacreate/', csrf_exempt(views.cuenta_create), name='cuentaCreate'),
]