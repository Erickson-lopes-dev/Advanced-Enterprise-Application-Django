from django.db import models
from apps.funcionarios.models import Funcionario


class RegistroHoraExtra(models.Model):
    motivo = models.CharField(max_length=100)

    # caso o usuário seja deletado seu registro continuara
    funcionario = models.ForeignKey(Funcionario, on_delete=models.PROTECT)

    def __str__(self):
        return self.motivo
