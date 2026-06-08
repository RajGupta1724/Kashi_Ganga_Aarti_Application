from django.conf import settings
from django.contrib import messages
from django.db.models import Avg
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.utils import timezone

from .forms import BookingForm, ServiceReviewForm
from .models import GalleryImage, ServiceReview, Testimonial


SERVICE_PAGE_DATA = {
    'wedding': {
        'page_title': 'Wedding Ganga Aarti Booking in Varanasi | Kashi Ganga',
        'meta_description': 'Book a private Wedding Ganga Aarti in Varanasi with Vedic rituals, floral arrangements, priest guidance, and sacred blessings at Assi Ghat or Dashashwamedh Ghat.',
        'meta_keywords': 'Wedding Ganga Aarti Varanasi, Wedding Ganga Aarti Booking, Private Wedding Aarti, Assi Ghat Wedding Ceremony, Dashashwamedh Ghat Wedding Aarti',
        'hero_badge': '💍 Wedding Special',
        'hero_title': 'Wedding Ganga Aarti in Varanasi',
        'hero_subtitle': 'A sacred ceremony for couples who want to begin married life with blessings from Maa Ganga.',
        'hero_image': 'images/wedding.jpeg',
        'hero_image_alt': 'Wedding Ganga Aarti ceremony in Varanasi',
        'service_name': 'Wedding Ganga Aarti',
        'service_summary': 'A complete wedding ceremony package with Vedic chanting, floral offerings, and priest-led arrangements at the ghats or your chosen venue.',
        'overview_paragraphs': [
            'A Wedding Ganga Aarti adds spiritual depth to the wedding day and creates a memorable blessing ceremony for the couple, family, and guests. We coordinate the rituals, lamps, flowers, and timing so the ceremony feels peaceful and well organized.',
            'Families often choose this service for a pre-wedding blessing, a post-ceremony ritual, or a private ghat experience that combines sacred tradition with beautiful photography opportunities. Our team handles the ceremony flow while the priest focuses on authentic Vedic invocation.',
            'If you are looking for a wedding ceremony that feels more meaningful than a standard event package, this page is for you. We can arrange the ritual at Assi Ghat, Dashashwamedh Ghat, or another location in Varanasi based on your plan.',
        ],
        'highlights': [
            'Full Vedic rituals and mantras',
            'Floral and diya arrangements',
            'Priest-led guidance for families',
            'Photography-friendly ceremony flow',
            'Private and public ghat options',
            'Custom timing based on auspicious muhurat',
        ],
        'service_areas': [
            'Assi Ghat Wedding Aarti',
            'Dashashwamedh Ghat Wedding Aarti',
            'Private wedding ceremonies at your venue',
            'Pre-wedding and post-wedding blessings',
        ],
        'process_steps': [
            'Share your preferred date, timing, and guest count.',
            'We confirm the ritual format, location, and priest availability.',
            'Our team prepares flowers, lamps, and ceremony essentials.',
            'You arrive for the ceremony and we guide the full ritual sequence.',
        ],
        'faqs': [
            {
                'question': 'Can Wedding Ganga Aarti be arranged for small family gatherings?',
                'answer': 'Yes. We regularly arrange intimate wedding blessings for small families as well as larger ceremonial groups.',
            },
            {
                'question': 'Do you provide arrangements at Assi Ghat and Dashashwamedh Ghat?',
                'answer': 'Yes. Both ghats can be arranged depending on the timing, crowd conditions, and your preferred ceremony style.',
            },
            {
                'question': 'Can photography be included during the ritual?',
                'answer': 'Yes, photography is usually welcome when it does not interrupt the devotion or movement of the ceremony.',
            },
        ],
        'related_pages': [
            {'label': 'Birthday Ganga Aarti', 'url_name': 'birthday_ganga_aarti'},
            {'label': 'Anniversary Ganga Aarti', 'url_name': 'anniversary_ganga_aarti'},
            {'label': 'Private Ganga Aarti', 'url_name': 'private_ganga_aarti'},
        ],
        'whatsapp_message': 'Namaste! I would like to book Wedding Ganga Aarti in Varanasi.',
    },
    'birthday': {
        'page_title': 'Birthday Ganga Aarti in Varanasi | Kashi Ganga',
        'meta_description': 'Celebrate with a Birthday Ganga Aarti in Varanasi. Arrange a private spiritual ceremony with blessings, prasad, priest guidance, and ghat arrangements.',
        'meta_keywords': 'Birthday Ganga Aarti Varanasi, Birthday Aarti Booking, Private Birthday Ceremony, Assi Ghat Birthday Puja, Ganga Aarti for Birthdays',
        'hero_badge': '🎂 Birthday Blessing',
        'hero_title': 'Birthday Ganga Aarti in Varanasi',
        'hero_subtitle': 'Celebrate life with a devotional ceremony that brings blessings, gratitude, and peace.',
        'hero_image': 'images/aarti.jpeg',
        'hero_image_alt': 'Birthday Ganga Aarti ceremony at the ghats of Varanasi',
        'service_name': 'Birthday Ganga Aarti',
        'service_summary': 'A warm and meaningful birthday ceremony with prayers, diya offerings, and family participation at the holy Ganga.',
        'overview_paragraphs': [
            'A Birthday Ganga Aarti is ideal for anyone who wants to start a new year of life with gratitude and divine blessings. It is a calming, family-friendly ceremony that feels personal and memorable.',
            'We can organize a birthday ritual for children, adults, or elders. The ceremony may include sankalp, chanting, flowers, aarti, and prasad, with a format adapted to the size and age of your group.',
            'For families visiting Varanasi, this is a special way to combine celebration, pilgrimage, and a shared spiritual experience at Assi Ghat or another sacred location.',
        ],
        'highlights': [
            'Personal birthday sankalp and prayers',
            'Family-friendly ritual planning',
            'Prasad and devotional offerings',
            'Sunrise or sunset booking options',
            'Ideal for children and elders',
            'Professional ghat coordination',
        ],
        'service_areas': [
            'Birthday Ganga Aarti at Assi Ghat',
            'Birthday blessings at Dashashwamedh Ghat',
            'Private birthday puja for families',
            'Travel-friendly arrangements for visitors',
        ],
        'process_steps': [
            'Tell us the date, age group, and preferred ghat.',
            'We suggest the right time and ritual format for your celebration.',
            'Our team arranges the flowers, lamps, and priest coordination.',
            'You participate in a peaceful and meaningful birthday blessing.',
        ],
        'faqs': [
            {
                'question': 'Can the birthday ceremony be kept short and simple?',
                'answer': 'Yes. We can arrange a compact but complete ritual for families who want a smaller celebration.',
            },
            {
                'question': 'Is this suitable for children?',
                'answer': 'Yes. Birthday Ganga Aarti is suitable for children and can be made light, warm, and family-friendly.',
            },
            {
                'question': 'Can we include cake or a private family meal after the ritual?',
                'answer': 'Yes, many families plan a private celebration after the ceremony and we can help coordinate the timing.',
            },
        ],
        'related_pages': [
            {'label': 'Wedding Ganga Aarti', 'url_name': 'wedding_ganga_aarti'},
            {'label': 'Anniversary Ganga Aarti', 'url_name': 'anniversary_ganga_aarti'},
            {'label': 'Corporate Ganga Aarti', 'url_name': 'corporate_ganga_aarti'},
        ],
        'whatsapp_message': 'Namaste! I would like to book Birthday Ganga Aarti in Varanasi.',
    },
    'anniversary': {
        'page_title': 'Anniversary Ganga Aarti in Varanasi | Kashi Ganga',
        'meta_description': 'Book an Anniversary Ganga Aarti in Varanasi for couples who want a devotional, private, and memorable celebration at the holy ghats.',
        'meta_keywords': 'Anniversary Ganga Aarti Varanasi, Anniversary Aarti Booking, Couple Aarti Ceremony, Private Anniversary Puja, Varanasi Ghat Ceremony',
        'hero_badge': '💑 Anniversary Special',
        'hero_title': 'Anniversary Ganga Aarti in Varanasi',
        'hero_subtitle': 'Renew your bond with a sacred ceremony that honors love, gratitude, and shared blessings.',
        'hero_image': 'images/wedd.jpeg',
        'hero_image_alt': 'Anniversary Ganga Aarti ceremony for couples in Varanasi',
        'service_name': 'Anniversary Ganga Aarti',
        'service_summary': 'A couple-focused ceremony with priest guidance, offerings, and a peaceful ghat setup for an anniversary celebration.',
        'overview_paragraphs': [
            'An Anniversary Ganga Aarti is a beautiful way for couples to mark another year together with devotion instead of a standard party. The ceremony feels calm, meaningful, and memorable.',
            'We can arrange a short private prayer, a couple sankalp, flower offerings, and a guided aarti that keeps the focus on togetherness and blessings. It works well for milestone anniversaries and intimate family gatherings.',
            'Many couples choose the ghats of Varanasi because the atmosphere naturally lends itself to gratitude, reflection, and a shared spiritual experience.',
        ],
        'highlights': [
            'Couple-focused spiritual planning',
            'Private blessing and sankalp options',
            'Flower and diya arrangements',
            'Sunrise, sunset, or evening timing',
            'Photography-friendly ceremony flow',
            'Ideal for milestone anniversaries',
        ],
        'service_areas': [
            'Anniversary Aarti at Assi Ghat',
            'Anniversary ceremonies at Dashashwamedh Ghat',
            'Private couple rituals and vow renewal',
            'Family-anniversary devotional gatherings',
        ],
        'process_steps': [
            'Share your anniversary date and preferred ceremony style.',
            'We confirm the ghat, priest, and timing for your ceremony.',
            'Our team prepares the ritual setup and offerings.',
            'You enjoy a calm, meaningful celebration with blessings.',
        ],
        'faqs': [
            {
                'question': 'Can the ceremony include a vow-renewal style blessing?',
                'answer': 'Yes. We can shape the experience like a vow renewal while keeping the ritual authentic and devotional.',
            },
            {
                'question': 'Is this suitable for a small private celebration?',
                'answer': 'Yes. Anniversary Ganga Aarti is often arranged as a private family or couple ceremony.',
            },
            {
                'question': 'Can you help us choose the right ghat for photos?',
                'answer': 'Yes. We can recommend a ghat and time that fit the atmosphere you want for the celebration and photos.',
            },
        ],
        'related_pages': [
            {'label': 'Wedding Ganga Aarti', 'url_name': 'wedding_ganga_aarti'},
            {'label': 'Birthday Ganga Aarti', 'url_name': 'birthday_ganga_aarti'},
            {'label': 'Private Ganga Aarti', 'url_name': 'private_ganga_aarti'},
        ],
        'whatsapp_message': 'Namaste! I would like to book Anniversary Ganga Aarti in Varanasi.',
    },
    'private': {
        'page_title': 'Private Ganga Aarti in Varanasi | Kashi Ganga',
        'meta_description': 'Arrange a private Ganga Aarti in Varanasi for family functions, special blessings, and custom rituals at Assi Ghat or Dashashwamedh Ghat.',
        'meta_keywords': 'Private Ganga Aarti Varanasi, Private Aarti Booking, Family Ganga Aarti, Assi Ghat Private Ceremony, Dashashwamedh Ghat Aarti',
        'hero_badge': '🪔 Private Ceremony',
        'hero_title': 'Private Ganga Aarti in Varanasi',
        'hero_subtitle': 'Custom ceremonies designed around your family, your occasion, and your preferred pace.',
        'hero_image': 'images/hero-aarti.jpg',
        'hero_image_alt': 'Private Ganga Aarti ceremony in Varanasi',
        'service_name': 'Private Ganga Aarti',
        'service_summary': 'Flexible private aarti arrangements for families who want a quieter, more personalized ritual experience.',
        'overview_paragraphs': [
            'Private Ganga Aarti is the right choice when you want the sacred ceremony without the pressure of a large public event. We can keep the ritual intimate, focused, and aligned with your family’s needs.',
            'This service is often booked for family blessings, guest visits, memorial rituals, pilgrim experiences, or any occasion that deserves a calm devotional atmosphere at the ghats of Varanasi.',
            'We help you plan the location, priest, timing, and ritual length so the experience feels respectful, efficient, and spiritually complete.',
        ],
        'highlights': [
            'Fully private or semi-private arrangements',
            'Custom ritual length and format',
            'Family-only participation options',
            'Ghat or venue-based planning',
            'Suitable for small groups and VIP guests',
            'Clear support before and during the ceremony',
        ],
        'service_areas': [
            'Private Aarti at Assi Ghat',
            'Private Aarti at Dashashwamedh Ghat',
            'Family ceremonies and pilgrim groups',
            'Special blessing services at custom venues',
        ],
        'process_steps': [
            'Tell us how private you want the ceremony to be.',
            'We suggest the best ghat, timing, and ritual flow.',
            'Our team prepares the necessary materials and coordination.',
            'You receive a calm, personalized ceremony with full guidance.',
        ],
        'faqs': [
            {
                'question': 'Can the ceremony be arranged for just my family?',
                'answer': 'Yes. Private Ganga Aarti can be arranged for a small family group or even a couple of close guests.',
            },
            {
                'question': 'Can you customize the ritual length?',
                'answer': 'Yes. We can keep the ceremony shorter or more detailed depending on your schedule and purpose.',
            },
            {
                'question': 'Is this only for weddings and birthdays?',
                'answer': 'No. Private Ganga Aarti can be arranged for many family and spiritual occasions, including custom blessings and pilgrimages.',
            },
        ],
        'related_pages': [
            {'label': 'Wedding Ganga Aarti', 'url_name': 'wedding_ganga_aarti'},
            {'label': 'Birthday Ganga Aarti', 'url_name': 'birthday_ganga_aarti'},
            {'label': 'Corporate Ganga Aarti', 'url_name': 'corporate_ganga_aarti'},
        ],
        'whatsapp_message': 'Namaste! I would like to book a private Ganga Aarti in Varanasi.',
    },
    'corporate': {
        'page_title': 'Corporate Ganga Aarti in Varanasi | Kashi Ganga',
        'meta_description': 'Book a Corporate Ganga Aarti in Varanasi for team blessings, client ceremonies, brand events, and professional spiritual gatherings.',
        'meta_keywords': 'Corporate Ganga Aarti Varanasi, Corporate Ceremony Booking, Team Blessing Ceremony, Business Aarti, Client Event Ganga Aarti',
        'hero_badge': '🏢 Corporate Event',
        'hero_title': 'Corporate Ganga Aarti in Varanasi',
        'hero_subtitle': 'A professional yet devotional ceremony for teams, clients, and business milestones.',
        'hero_image': 'images/aarti2.jpeg',
        'hero_image_alt': 'Corporate Ganga Aarti ceremony in Varanasi',
        'service_name': 'Corporate Ganga Aarti',
        'service_summary': 'A polished ceremony format for companies that want a meaningful team blessing or client-facing spiritual experience.',
        'overview_paragraphs': [
            'Corporate Ganga Aarti is designed for companies, founders, and teams who want a memorable event that feels both culturally respectful and professionally managed. It works well for team blessings, launches, appreciation events, and client gatherings.',
            'We keep the ceremony organized so your guests can participate comfortably while the priest and support team handle the ritual details. The result is a smooth and dignified event in a unique spiritual setting.',
            'If your company wants an experience that stands out from standard banquet programming, a Ganga Aarti ceremony in Varanasi can create a strong and memorable impression.',
        ],
        'highlights': [
            'Team and client blessing arrangements',
            'Structured coordination for corporate guests',
            'Event-friendly ceremony pacing',
            'Photo and video friendly setup',
            'Suitable for launches and milestone events',
            'Professional communication before the event',
        ],
        'service_areas': [
            'Corporate ceremonies at Assi Ghat',
            'Corporate ceremonies at Dashashwamedh Ghat',
            'Founder blessings and milestone events',
            'Team outings and client experiences',
        ],
        'process_steps': [
            'Share your event objective, headcount, and timing.',
            'We shape a ceremony that fits your brand and schedule.',
            'Our team coordinates priest, materials, and guest flow.',
            'Your team experiences a polished spiritual event with guidance.',
        ],
        'faqs': [
            {
                'question': 'Can this be arranged for a company offsite or retreat?',
                'answer': 'Yes. Corporate Ganga Aarti works well for offsites, retreats, and special team gatherings.',
            },
            {
                'question': 'Can you keep the event formal and well organized?',
                'answer': 'Yes. We focus on clear timing, guest flow, and a polished ceremony structure for corporate groups.',
            },
            {
                'question': 'Can branding be included without disturbing the ritual?',
                'answer': 'Yes. We can usually coordinate light branding or event mentions in a way that respects the ceremony.',
            },
        ],
        'related_pages': [
            {'label': 'Wedding Ganga Aarti', 'url_name': 'wedding_ganga_aarti'},
            {'label': 'Private Ganga Aarti', 'url_name': 'private_ganga_aarti'},
            {'label': 'Anniversary Ganga Aarti', 'url_name': 'anniversary_ganga_aarti'},
        ],
        'whatsapp_message': 'Namaste! I would like to book Corporate Ganga Aarti in Varanasi.',
    },
}


def _service_page_context(request, page_key):
    whatsapp_number = getattr(settings, 'WHATSAPP_NUMBER', '919235054005')
    page = SERVICE_PAGE_DATA[page_key]
    return {
        **page,
        'whatsapp_number': whatsapp_number,
    }


def _render_service_page(request, page_key):
    return render(request, 'service_landing_page.html', _service_page_context(request, page_key))


def sitemap_xml(request):
    # Use current timezone-aware timestamp for sitemap <lastmod>
    lastmod_now = timezone.now().isoformat()
    xml = render_to_string('sitemap.xml', {'lastmod_now': lastmod_now}, request=request)
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


def _service_review_context(request, review_form=None):
    active_reviews = ServiceReview.objects.filter(is_active=True)
    review_stats = active_reviews.aggregate(average_rating=Avg('rating'))
    average_service_rating = round(review_stats['average_rating'] or 0, 1)
    service_review_count = active_reviews.count()

    return {
        'review_form': review_form or ServiceReviewForm(),
        'recent_reviews': active_reviews[:6],
        'average_service_rating': average_service_rating,
        'service_review_count': service_review_count,
    }


def index(request):
    testimonials = Testimonial.objects.filter(is_active=True)[:6]
    gallery_preview = GalleryImage.objects.filter(is_active=True)[:6]

    if request.method == 'POST':
        review_form = ServiceReviewForm(request.POST)
        if review_form.is_valid():
            review_form.save()
            messages.success(
                request,
                'Thanks for your rating. Your feedback helps other visitors choose the right service.'
            )
            return redirect('ratings')
    else:
        review_form = ServiceReviewForm()

    review_context = _service_review_context(request, review_form)

    return render(request, 'index.html', {
        'testimonials': testimonials,
        'gallery_preview': gallery_preview,
        **review_context,
    })


def about(request):
    whatsapp_number = getattr(settings, 'WHATSAPP_NUMBER', '919235054005')
    site_address = getattr(settings, 'SITE_ADDRESS', 'Assi Ghat, Varanasi, UP, India')
    site_email = getattr(settings, 'SITE_EMAIL', 'booking@kashiganga.in')
    site_phone_primary = getattr(settings, 'SITE_PHONE_PRIMARY', None)
    return render(request, 'about.html', {
        'whatsapp_number': whatsapp_number,
        'site_address': site_address,
        'site_email': site_email,
        'site_phone_primary': site_phone_primary,
    })


def ratings(request):
    if request.method == 'POST':
        review_form = ServiceReviewForm(request.POST)
        if review_form.is_valid():
            review_form.save()
            messages.success(
                request,
                'Thanks for your rating. Your feedback helps other visitors choose the right service.'
            )
            return redirect('ratings')
    else:
        review_form = ServiceReviewForm()

    return render(request, 'ratings.html', _service_review_context(request, review_form))


def home(request):
    return index(request)


def robots_txt(request):
    site_root = f'{request.scheme}://{request.get_host()}'
    content = (
        'User-agent: *\n'
        'Allow: /\n'
        f'Sitemap: {site_root}/sitemap.xml\n'
    )
    return HttpResponse(content, content_type='text/plain')


def services(request):
    whatsapp_number = getattr(settings, 'WHATSAPP_NUMBER', '919235054005')
    return render(request, 'services.html', {'whatsapp_number': whatsapp_number})


def wedding_ganga_aarti(request):
    return _render_service_page(request, 'wedding')


def birthday_ganga_aarti(request):
    return _render_service_page(request, 'birthday')


def anniversary_ganga_aarti(request):
    return _render_service_page(request, 'anniversary')


def private_ganga_aarti(request):
    return _render_service_page(request, 'private')


def corporate_ganga_aarti(request):
    return _render_service_page(request, 'corporate')


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
