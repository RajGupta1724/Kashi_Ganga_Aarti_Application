from django.contrib import admin

from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve as static_serve

admin.site.site_header = "Kashi Ganga Admin Panel"
admin.site.site_title = "Kashi Ganga"
admin.site.index_title = "Manage Bookings & Content"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
] + [
    re_path(r'^sitemap\.xml$', static_serve, {'path': 'sitemap.xml', 'document_root': settings.STATIC_ROOT}, name='sitemap'),
    re_path(r'^robots\.txt$', static_serve, {'path': 'robots.txt', 'document_root': settings.STATIC_ROOT}, name='robots'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
