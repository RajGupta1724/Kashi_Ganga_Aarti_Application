from django.conf import settings
from django.contrib import messages
from django.db.models import Avg
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string

from .forms import BookingForm, ServiceReviewForm
from .models import GalleryImage, ServiceReview, Testimonial


def sitemap_xml(request):
    xml = render_to_string('sitemap.xml')
    return HttpResponse(xml, content_type='application/xml')


def kashi_ganga_aarti_timing(request):
    return render(request, 'kashi_ganga_aarti_timing.html')


def ganga_aarti_booking(request):
    return render(request, 'ganga_aarti_booking.html')


def dashashwamedh_ghat_aarti(request):
    return render(request, 'dashashwamedh_ghat_aarti.html')


def disclaimer(request):
    return render(request, 'disclaimer.html')


def privacy_policy(request):
    return render(request, 'privacy_policy.html')


def index(request):
    testimonials = Testimonial.objects.filter(is_active=True)[:6]
    gallery_preview = GalleryImage.objects.filter(is_active=True)[:6]
    active_reviews = ServiceReview.objects.filter(is_active=True)
    review_stats = active_reviews.aggregate(average_rating=Avg('rating'))
    average_service_rating = round(review_stats['average_rating'] or 0, 1)
    service_review_count = active_reviews.count()
    recent_reviews = active_reviews[:6]

    if request.method == 'POST':
        review_form = ServiceReviewForm(request.POST)
        if review_form.is_valid():
            review_form.save()
            messages.success(
                request,
                'Thanks for your rating. Your feedback helps other visitors choose the right service.'
            )
            return redirect('home')
    else:
        review_form = ServiceReviewForm()

    return render(request, 'index.html', {
        'testimonials': testimonials,
        'gallery_preview': gallery_preview,
        'review_form': review_form,
        'recent_reviews': recent_reviews,
        'average_service_rating': average_service_rating,
        'service_review_count': service_review_count,
    })


def about(request):
    return render(request, 'about.html')


def home(request):
    return index(request)


def robots_txt(request):
    content = (
        'User-agent: *\n'
        'Allow: /\n'
        'Sitemap: https://kashigangaaarti.in/sitemap.xml\n'
    )
    return HttpResponse(content, content_type='text/plain')


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


def health(request):
    return JsonResponse({'status': 'ok'})
