from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('novedad/', views.novedad_list),
    path('novedadcreate/', csrf_exempt(views.novedad_create), name='novedadCreate'),
]