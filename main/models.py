from django.db import models
from django.core.validators import RegexValidator


phone_validator = RegexValidator(
    regex=r'^\+?1?\d{9,15}$',
    message="Enter a valid phone number (9–15 digits, optionally starting with +)."
)


class Booking(models.Model):
    EVENT_CHOICES = [
        ('wedding',      'Wedding Ganga Aarti'),
        ('birthday',     'Birthday Aarti'),
        ('anniversary',  'Anniversary Aarti'),
        ('spiritual',    'Special Spiritual Ceremony'),
        ('satyanarayan', 'Satyanarayan Puja'),
        ('mundan',       'Mundan Ceremony'),
        ('other',        'Other'),
    ]

    STATUS_CHOICES = [
        ('pending',   'Pending'),
        ('confirmed', 'Confirmed'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    name       = models.CharField(max_length=200, verbose_name="Full Name")
    phone      = models.CharField(max_length=15, validators=[phone_validator], verbose_name="Phone Number")
    email      = models.EmailField(verbose_name="Email Address")
    event_type = models.CharField(max_length=50, choices=EVENT_CHOICES, verbose_name="Event Type")
    event_date = models.DateField(verbose_name="Event Date")
    location   = models.CharField(max_length=500, verbose_name="Event Location")
    message    = models.TextField(blank=True, verbose_name="Additional Message")
    status     = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name="Status")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Booking Inquiry'
        verbose_name_plural = 'Booking Inquiries'

    def __str__(self):
        return f"{self.name} — {self.get_event_type_display()} on {self.event_date}"


class Testimonial(models.Model):
    name       = models.CharField(max_length=200)
    location   = models.CharField(max_length=200, blank=True)
    event_type = models.CharField(max_length=100)
    message    = models.TextField()
    rating     = models.PositiveSmallIntegerField(default=5)
    image      = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    is_active  = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} — {self.event_type}"


class GalleryImage(models.Model):
    CATEGORY_CHOICES = [
        ('wedding',      'Wedding'),
        ('birthday',     'Birthday'),
        ('anniversary',  'Anniversary'),
        ('ceremony',     'Ceremony'),
        ('ganga_aarti',  'Ganga Aarti'),
        ('other',        'Other'),
    ]

    title      = models.CharField(max_length=200)
    image      = models.ImageField(upload_to='gallery/')
    category   = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='ceremony')
    caption    = models.CharField(max_length=300, blank=True)
    is_active  = models.BooleanField(default=True)
    order      = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']
        verbose_name = 'Gallery Image'
        verbose_name_plural = 'Gallery Images'

    def __str__(self):
        return self.title
