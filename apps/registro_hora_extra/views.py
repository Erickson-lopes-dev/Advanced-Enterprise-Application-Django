from django.views.generic import ListView

from apps.registro_hora_extra.models import RegistroHoraExtra


class HoraExtraList(ListView):
    model = RegistroHoraExtra

    # busca apenas o da empresa do usuário logado
    def get_queryset(self):
        # pegar a empresa do usuario logago
        empresa_logada = self.request.user.funcionario.empresa
        # Filtrar funcionarios que tenha a mesma empresa do user logado
        return RegistroHoraExtra.objects.filter(funcionario__empresa=empresa_logada)
