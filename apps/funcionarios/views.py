from django.views.generic import ListView

from apps.funcionarios.models import Funcionario


class FuncionariosList(ListView):
    model = Funcionario

    def get_queryset(self):
        # pegar a empresa do usuario logago
        empresa_logada = self.request.user.funcionario.empresa
        # Filtrar funcionarios que tenha a mesma empresa do user logado
        return Funcionario.objects.filter(empresa=empresa_logada)
