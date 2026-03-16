from django.urls import path
from . import views

urlpatterns = [
    path('',           views.index,           name='index'),
    path('',           views.index,           name='home'),
    path('services/',  views.services,        name='services'),
    path('gallery/',   views.gallery,         name='gallery'),
    path('about/',     views.about,           name='about'),
    path('booking/',   views.booking,         name='booking'),
    path('booking/success/', views.booking_success, name='booking_success'),
]
