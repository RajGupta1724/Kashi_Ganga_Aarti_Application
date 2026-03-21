from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # 👇 This line connects your entire app
    path('', include('main.urls')),
]
