from django.conf import settings


def site_context(request):
    return {
        'whatsapp_number': getattr(settings, 'WHATSAPP_NUMBER', '919235054005'),
        'site_name': 'Kashi Ganga',
        'site_phone_primary': '+91 92350 54005',
        'site_email': 'rajgupta1782005@gmail.com',
        'site_address': 'Assi Ghat, Varanasi, Uttar Pradesh 221005',
    }
