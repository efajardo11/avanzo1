from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('descuento/', views.descuento_list),
    path('descuentoCreate/', csrf_exempt(views.descuento_create), name='descuentoCreate'),
]