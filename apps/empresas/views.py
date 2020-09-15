from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView

from apps.empresas.models import Empresa


class EmpresaCreate(CreateView):
    model = Empresa
    fields = ['nome']

    def form_valid(self, form):
        # cria um objeto com o form
        obj = form.save()
        # Pega os dados do usuário referente ao funcionario
        funcionario = self.request.user.funcionario
        # Pega a empresa do funcionario
        funcionario.empresa = obj
        # Salva a empresa do funcionario
        funcionario.save()

        return HttpResponse('OK')

        # para que apenas os usuarios da empresa possa alterar ela


class EmpresaEdit(UpdateView):
    model = Empresa
    fields = ['nome']
    # success_url = '/blog/'
