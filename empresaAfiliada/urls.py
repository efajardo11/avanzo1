from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('empresa/', views.empresa_list),
    path('empresacreate/', csrf_exempt(views.empresa_create), name='empresaCreate'),
]