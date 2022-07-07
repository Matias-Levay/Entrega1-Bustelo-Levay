from django.urls import path
from inicio.views import vista_inicio, leerEquipos, equipos, editarEquipo, eliminarEquipo

urlpatterns = [
    path('', vista_inicio),
    path('leerEquipos', leerEquipos, name='LeerEquipos'),
    path('equipos', equipos, name='equipos'),
    path('editarEquipo/<equipo_nombre>/', editarEquipo, name = 'EditarEquipo'),
    path('eliminarEquipo/<equipo_nombre>/', eliminarEquipo, name = 'EliminarEquipo'),
]
