
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.conf import settings
from django.contrib import messages
from .forms import BookingForm
from .models import Testimonial, GalleryImage


def index(request):
    testimonials = Testimonial.objects.filter(is_active=True)[:6]
    gallery_preview = GalleryImage.objects.filter(is_active=True)[:6]
    whatsapp_number = getattr(settings, 'WHATSAPP_NUMBER', '919235054005')
    return render(request, 'index.html', {
        'testimonials': testimonials,
        'gallery_preview': gallery_preview,
        'whatsapp_number': whatsapp_number,
    })


def home(request):
        'active_category': category,
    })


def about(request):
    return render(request, 'about.html')
   
    def booking(request):
        whatsapp_number = getattr(settings, 'WHATSAPP_NUMBER', '919235054005')
        if request.method == 'POST':
            form = BookingForm(request.POST)
            if form.is_valid():
                form.save()
        else:
