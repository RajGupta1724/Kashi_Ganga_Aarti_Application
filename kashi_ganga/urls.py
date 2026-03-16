from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "Kashi Ganga Admin Panel"
admin.site.site_title = "Kashi Ganga"
admin.site.index_title = "Manage Bookings & Content"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
