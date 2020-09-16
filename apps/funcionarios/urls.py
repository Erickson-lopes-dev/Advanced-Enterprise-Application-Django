from django.urls import path

from apps.funcionarios.views import FuncionariosList

urlpatterns = [
    path('', FuncionariosList.as_view(), name='list_funcionarios')
]
