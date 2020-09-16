from django.urls import path

from apps.departamentos.views import DepartamentosList

urlpatterns = [
    path('list', DepartamentosList.as_view(), name='list_departamentos'),
    # path('novo/', DepartamentosList.as_view(), name='novo_departamentos'),
    # path('update/<int:pk/>', DepartamentosList.as_view(), name='update_departamentos'),
    # path('delete/<int:pk/>', DepartamentosList.as_view(), name='delete_departamentos'),
]
