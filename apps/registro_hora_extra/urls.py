from django.urls import path

from .views import HoraExtraList, HoraExtraUpdate, HoraExtraDElete, HoraExtraCreate

urlpatterns = [
    path('', HoraExtraList.as_view(), name='list_hora_extra'),
    path('editar/<int:pk>/', HoraExtraUpdate.as_view(), name='update_hora_extra'),
    path('delete/<int:pk>/', HoraExtraDElete.as_view(), name='delete_hora_extra'),
    path('novo/', HoraExtraCreate.as_view(), name='create_hora_extra'),

]
