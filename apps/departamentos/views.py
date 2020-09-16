from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from apps.departamentos.models import Departamento


class DepartamentosList(ListView):
    model = Departamento

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Departamento.objects.filter(empresa=empresa_logada)


class DepartamentosCreate(CreateView):
    model = Departamento
    fields = ['nome']

    def form_valid(self, form):
        departamento = form.save(commit=False)
        # pegar a empresa em que o usuario logado esta registrado salvando o dado no campo
        departamento.empresa = self.request.user.funcionario.empresa
        departamento.save()
        return super(DepartamentosCreate, self).form_valid(form)

    success_url = reverse_lazy('list_departamentos')


class DepartamentosUpdate(UpdateView):
    model = Departamento
    fields = ['nome']

    success_url = reverse_lazy('list_departamentos')


class DepartamentosDelete(DeleteView):
    model = Departamento
    success_url = reverse_lazy('list_departamentos')
