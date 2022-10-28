from django.urls import path
from .models import Hardware, Software, Insumos, Celulares
from .views import celulares, hardware, inicio, insumos,software


urlpatterns = [
    path(" ", inicio),
    path ("lista_celulares/", celulares),
    path ("lista_hardware/", hardware),
    path ("lista_insumos/", insumos),
    path ("lista_software/", software),
]
