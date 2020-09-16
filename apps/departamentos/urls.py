from django.urls import path

from apps.departamentos.views import DepartamentosList, DepartamentosCreate, DepartamentosUpdate, DepartamentosDelete

urlpatterns = [
    path('list', DepartamentosList.as_view(), name='list_departamentos'),
    path('novo/', DepartamentosCreate.as_view(), name='novo_departamento'),
    path('update/<int:pk>/', DepartamentosUpdate.as_view(), name='update_departamento'),
    path('delete/<int:pk>/', DepartamentosDelete.as_view(), name='delete_departamento'),
]
