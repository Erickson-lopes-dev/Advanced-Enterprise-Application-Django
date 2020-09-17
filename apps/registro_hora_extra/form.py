from django.forms import ModelForm
from apps.funcionarios.models import Funcionario
from apps.registro_hora_extra.models import RegistroHoraExtra


class RegistroHoraExtraForm(ModelForm):
    # colocar apenas os usuários da empresa do user / filtrar usuario pela empresa
    def __init__(self, user, *args, **kwargs):
        super(RegistroHoraExtraForm, self).__init__(*args, **kwargs)
        self.fields['funcionario'].queryset = Funcionario.objects.filter(empresa=user.funcionario.empresa)

    class Meta:
        model = RegistroHoraExtra
        fields = ['motivo', 'funcionario', 'horas']
