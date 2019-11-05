from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('asesoria/', include('apps.asesoria.urls')),
    path('api-auth/', include('rest_framework.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
