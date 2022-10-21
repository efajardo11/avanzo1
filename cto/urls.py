from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('cto/', views.cto_list),
    path('ctocreate/', csrf_exempt(views.cto_create), name='ctoCreate'),
]