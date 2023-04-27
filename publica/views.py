from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader

def index(request):
    if (request.method=='GET'):
        titulo='Titulo cuando accedo por GET'
        
    else:
        titulo='Cuando accedo por otro metodo'
        parametro_uno=request.GET.get('param')
        parametro_dos=request.GET.get('param2')
    return render(request,'publica/index.html')
def menu(request):
    template = loader.get_template('publica/menu.html')
    context = {'titulo':'menu'}
    return HttpResponse(template.render(context,request))
def pedido(request):
    template = loader.get_template('publica/pedido.html')
    context = {'titulo':'pedido'}
    return HttpResponse(template.render(context,request))
def promociones(request):
    template = loader.get_template('publica/promociones.html')
    context = {'titulo':'promociones'}
    return HttpResponse(template.render(context,request))


    #return HttpResponse(f"""<h1>Django</h1><p>{titulo}</p><p>Parametro uno recibido:{parametro_uno}</p><p>Parametro dos recibido:{parametro_dos}</p>
    #<form action='' method='POST'><input type='submit' value='enviar'></form>""")
