from django.shortcuts import render
from .forms import ContactoForm
from .models import Consulta

def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            consulta = Consulta(nombre=form.cleaned_data['nombre'],
                               email=form.cleaned_data['email'],
                               asunto=form.cleaned_data['asunto'],
                               mensaje=form.cleaned_data['mensaje'],
                               tipo_consulta=form.cleaned_data['tipo_consulta'],
                               suscripcion=form.cleaned_data['suscripcion']
            )
            consulta.save()
            form = ContactoForm()  # Reinicializar el formulario
            
        return render(request, 'publica/exito.html', {'form': form, 'success': True})
    else:
        form = ContactoForm()
    
    return render(request, 'publica/contacto.html', {'form': form})


def index(request):
    if request.method == 'GET':
        titulo = 'Titulo cuando accedo por GET'
    else:
        titulo = 'Cuando accedo por otro método'
        parametro_uno = request.GET.get('param')
        parametro_dos = request.GET.get('param2')
    
    return render(request, 'publica/index.html', {'titulo': titulo})

def menu(request):
    context = {'titulo': 'menu'}
    return render(request, 'publica/menu.html', context)

def pedido(request):
    context = {'titulo': 'pedido'}
    return render(request, 'publica/pedido.html', context)

def promociones(request):
    context = {'titulo': 'promociones'}
    return render(request, 'publica/promociones.html', context)



