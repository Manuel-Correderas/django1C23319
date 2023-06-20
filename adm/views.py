from django.shortcuts import render
from .models import Tarea
from .forms import TareaForm

def index_adm(request):
    variable = 'Nombre'
    return render(request, 'adm/index_adm.html', {'variable': variable})

def tareas(request):
    tareas = Tarea.objects.all()
    context = {'tareas': tareas}
    return render(request, 'tareas.html', context)

def crear_tarea(request):
    if request.method == 'GET':
        return render(request,'crear_tarea.html', {
        'form': TareaForm
    })
    else:
        print(request.POST)
        return render(request,'crear_tarea.html', {
        'form': TareaForm})
    