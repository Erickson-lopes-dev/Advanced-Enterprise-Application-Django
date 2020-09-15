from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('apps.core.urls')),
    path('empresa/', include('apps.empresas.urls')),
    path('funcionario/', include('apps.funcionarios.urls')),
    path('accounts/', include('django.contrib.auth.urls'))
]
