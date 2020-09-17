from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.core.urls')),
    path('empresas/', include('apps.empresas.urls')),
    path('funcionarios/', include('apps.funcionarios.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('departamentos/', include('apps.departamentos.urls')),
    path('documento/', include('apps.documentos.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
