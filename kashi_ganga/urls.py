
from django.contrib import admin
from django.urls import path, include
from main.views import robots_txt, sitemap_xml  # 👈 ADD THIS

urlpatterns = [
    path('admin/', admin.site.urls),

    # 👇 Serve robots.txt DIRECTLY at root
    path('robots.txt', robots_txt),
    path('sitemap.xml', sitemap_xml),  # ✅ ADD THIS

    # 👇 All other routes
    path('', include('main.urls')),
]
