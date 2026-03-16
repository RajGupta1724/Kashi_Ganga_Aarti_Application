from django.shortcuts import render, redirect
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
    return index(request)


def services(request):
    whatsapp_number = getattr(settings, 'WHATSAPP_NUMBER', '919235054005')
    return render(request, 'services.html', {'whatsapp_number': whatsapp_number})


def gallery(request):
    category = request.GET.get('category', 'all')
    images = GalleryImage.objects.filter(is_active=True)
    if category != 'all':
        images = images.filter(category=category)
    categories = GalleryImage.CATEGORY_CHOICES
    return render(request, 'gallery.html', {
        'images': images,
        'categories': categories,
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
            messages.success(
                request,
                'Your booking request has been submitted! We will contact you shortly. 🙏'
            )
            return redirect('booking_success')
    else:
        form = BookingForm()
    return render(request, 'booking.html', {'form': form, 'whatsapp_number': whatsapp_number})


def booking_success(request):
    whatsapp_number = getattr(settings, 'WHATSAPP_NUMBER', '919235054005')
    return render(request, 'booking_success.html', {'whatsapp_number': whatsapp_number})
