from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Full Name')),
                ('phone', models.CharField(
                    max_length=15,
                    validators=[django.core.validators.RegexValidator(
                        regex=r'^\+?1?\d{9,15}$',
                        message="Enter a valid phone number (9–15 digits, optionally starting with +)."
                    )],
                    verbose_name='Phone Number'
                )),
                ('email', models.EmailField(verbose_name='Email Address')),
                ('event_type', models.CharField(
                    choices=[
                        ('wedding', 'Wedding Ganga Aarti'),
                        ('birthday', 'Birthday Aarti'),
                        ('anniversary', 'Anniversary Aarti'),
                        ('spiritual', 'Special Spiritual Ceremony'),
                        ('satyanarayan', 'Satyanarayan Puja'),
                        ('mundan', 'Mundan Ceremony'),
                        ('other', 'Other'),
                    ],
                    max_length=50, verbose_name='Event Type'
                )),
                ('event_date', models.DateField(verbose_name='Event Date')),
                ('location', models.CharField(max_length=500, verbose_name='Event Location')),
                ('message', models.TextField(blank=True, verbose_name='Additional Message')),
                ('status', models.CharField(
                    choices=[
                        ('pending', 'Pending'),
                        ('confirmed', 'Confirmed'),
                        ('completed', 'Completed'),
                        ('cancelled', 'Cancelled'),
                    ],
                    default='pending', max_length=20, verbose_name='Status'
                )),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={'ordering': ['-created_at'], 'verbose_name': 'Booking Inquiry', 'verbose_name_plural': 'Booking Inquiries'},
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('location', models.CharField(blank=True, max_length=200)),
                ('event_type', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('rating', models.PositiveSmallIntegerField(default=5)),
                ('image', models.ImageField(blank=True, null=True, upload_to='testimonials/')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={'ordering': ['-created_at']},
        ),
        migrations.CreateModel(
            name='GalleryImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='gallery/')),
                ('category', models.CharField(
                    choices=[
                        ('wedding', 'Wedding'),
                        ('birthday', 'Birthday'),
                        ('anniversary', 'Anniversary'),
                        ('ceremony', 'Ceremony'),
                        ('ganga_aarti', 'Ganga Aarti'),
                        ('other', 'Other'),
                    ],
                    default='ceremony', max_length=50
                )),
                ('caption', models.CharField(blank=True, max_length=300)),
                ('is_active', models.BooleanField(default=True)),
                ('order', models.PositiveIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={'ordering': ['order', '-created_at'], 'verbose_name': 'Gallery Image', 'verbose_name_plural': 'Gallery Images'},
        ),
    ]
