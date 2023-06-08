from django.shortcuts import render

def index_adm(request):
    variable = 'test variable'
    return render(request,'adm/index_adm.html', {'variable':variable }) 
# Create your views here.
