from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from infos.views import info_add_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", info_add_view, name="main-view"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
