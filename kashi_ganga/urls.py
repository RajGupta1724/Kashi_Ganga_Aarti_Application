
from django.contrib import admin
from django.urls import include, path

from main.views import robots_txt, sitemap_xml

urlpatterns = [
    path('admin/', admin.site.urls),
    path('robots.txt', robots_txt),
    path('sitemap.xml', sitemap_xml),
    path('', include('main.urls')),
]
