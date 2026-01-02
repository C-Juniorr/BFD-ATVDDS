from django.urls import path
from .views import index, FuncionarioListView

app_name = 'website'

urlpatterns = [
    path('', index, name='index'),
    path('funcionarios/', FuncionarioListView.as_view(), name='lista_funcionarios'),
]
