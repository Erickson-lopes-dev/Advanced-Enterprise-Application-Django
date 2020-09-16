from django.views.generic import ListView

from apps.funcionarios.models import Funcionario


class FuncionariosList(ListView):
    model = Funcionario
