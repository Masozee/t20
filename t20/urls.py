from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.sites.AdminSite.site_header = 'T20 INDONESIA 2022'
admin.sites.AdminSite.site_title = 'T20 INDONESIA 2022'
admin.sites.AdminSite.index_title = 'T20 INDONESIA 2022'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('web.url')),
    path('tinymce/', include('tinymce.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)