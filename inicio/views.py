from multiprocessing import context
from django.shortcuts import render
from django.db.models import Q
from inicio.forms import FormularioDeInscripcion, FormularioEncuesta, FormularioContactenos
from inicio.models import EquiposModel

# Create your views here.
def vista_inicio(request):
    if request.method == 'POST':
        if request.POST['action'] == 'Registrarme':
            form = FormularioDeInscripcion(request.POST)
            if form.is_valid():
                form.save()
                # form = FormularioDeInscripcion()
            else:
                form = FormularioDeInscripcion()
        elif request.POST['action'] == 'Encuesta':
            form = FormularioEncuesta(request.POST)
            if form.is_valid():
                form.save()
                # form = FormularioEncuesta()
            else:
                form = FormularioEncuesta()
        elif request.POST['action'] == 'Contactenos':
            form = FormularioContactenos(request.POST)
            if form.is_valid():
                form.save()
                # form = FormularioContactenos()
            else:
                form = FormularioContactenos()
        elif request.POST['action'] == 'Buscar':
            texto = request.POST.get('search')
            club = EquiposModel.objects.filter(Q(equipo__contains=texto) | Q(presidente__contains=texto) | Q(dt__contains=texto))
            if club:
                resultados = club
                contexto = {'resultados': resultados}
                return render(request, 'inicio/busqueda.html', contexto)

    form = FormularioDeInscripcion()
    form_encuesta = FormularioEncuesta()
    form_contactenos = FormularioContactenos()

    contexto = {'form': form, 'form_encuesta':form_encuesta, 'form_contactenos': form_contactenos}

    return render(request, 'inicio/inicio.html', contexto)