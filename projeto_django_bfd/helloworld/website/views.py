from django.shortcuts import render
from django.views.generic import ListView
from helloworld.models import Funcionario

def index(request):
    return render(request, 'website/index.html')

class FuncionarioListView(ListView):
    template_name = 'website/lista_funcionarios.html'
    model = Funcionario
    context_object_name = 'funcionarios'
