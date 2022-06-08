from django.urls import path
from inicio.views import vista_inicio

urlpatterns = [
    path('', vista_inicio),

]
