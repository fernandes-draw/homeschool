
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
]

# Adiciona as rotas do debug toolbar apenas se o DEBUG estiver ativado
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
        path('accounts/', include('allauth.urls')),
    ] + urlpatterns