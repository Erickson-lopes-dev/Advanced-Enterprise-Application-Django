from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from apps.departamentos.models import Departamento
from apps.empresas.models import Empresa


class Funcionario(models.Model):
    nome = models.CharField(max_length=100)

    # relacionando com usuario de um pra um
    user = models.OneToOneField(User, on_delete=models.PROTECT)

    # O usuário pode estar relacionado a multiplos departamentos
    departamentos = models.ManyToManyField(Departamento)

    # Relacionando o usuário a uma empresa
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT, null=True, blank=True)

    def get_absolute_url(self):
        return reverse('list_funcionarios')

    def __str__(self):
        return self.nome
