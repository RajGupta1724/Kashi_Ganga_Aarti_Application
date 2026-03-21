from django.urls import path
from . import views

urlpatterns = [
    path('',           views.index,           name='index'),
    path('',           views.index,           name='home'),
    path('health/',    views.health,          name='health'),
    path('services/',  views.services,        name='services'),
    path('gallery/',   views.gallery,         name='gallery'),
    path('about/',     views.about,           name='about'),
    path('booking/',   views.booking,         name='booking'),
    path('booking/success/', views.booking_success, name='booking_success'),

    # SEO pages
    path('kashi-ganga-aarti-timing/', views.kashi_ganga_aarti_timing, name='kashi_ganga_aarti_timing'),
    path('ganga-aarti-booking/', views.ganga_aarti_booking, name='ganga_aarti_booking'),
    path('dashashwamedh-ghat-aarti/', views.dashashwamedh_ghat_aarti, name='dashashwamedh_ghat_aarti'),
]
