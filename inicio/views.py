from multiprocessing import context
from django.shortcuts import render
from django.db.models import Q
from inicio.forms import FormularioDeInscripcion, FormularioEncuesta, FormularioContactenos, FormularioEquipo
from inicio.models import EquiposModel
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import login, logout, authenticate

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




def equipos(request):
    if request.method == 'POST':
        miFormulario = FormularioEquipo(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
        
        equipo = Equipo (equipo = informacion['equipo'], fundacion = informacion['fundacion'], presidente = informacion['presidente'], dt = informacion['dt'], division = informacion['division'])
        equipo.save()
        return render(request, 'inicio/inicio.html')
    else:
        miFormulario = FormularioEquipo()
    return render(request, 'inicio/equipos.html', {'miFormulario': miFormulario})


def leerEquipos(request):
    equipo = EquiposModel.objects.all() 
    contexto = {"equipo": equipo}
    return render(request, 'Inicio/leerEquipos.html', contexto)

def editarEquipo(request, equipo_nombre):
    equipo = EquiposModel.objects.get(equipo = equipo_nombre)

    if request.method == "POST":
        miFormulario = EquiposModel(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data

            equipo.nombre = informacion['equipo']
            equipo.fundacion = informacion['fundacion']
            equipo.presidente = informacion['presidente']
            equipo.dt = informacion['dt']
            equipo.division = informacion['division']

            profesor.save()

            return render(request, 'inicio/inicio.html')

    else:
        miFormulario = FormularioEquipo(initial={'equipo': equipo.equipo, 'fundacion': equipo.fundacion, 'presidente': equipo.presidente, 'dt': equipo.dt, 'division': equipo.division})

    return render(request, 'inicio/editarEquipo.html', {'miFormulario': miFormulario, 'equipo_nombre': equipo_nombre})

def eliminarEquipo(request, equipo_nombre):
    equipo = EquiposModel.objects.get(equipo = equipo_nombre)
    equipo.delete()

    equipo = Equipo.objects.all()
    contexto={"equipo": equipo}
    return render(request, 'inicio/leerEquipos.html', contexto)


