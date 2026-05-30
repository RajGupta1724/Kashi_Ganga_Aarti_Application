from django import forms
import datetime

from .models import Booking, ServiceReview


class BookingForm(forms.ModelForm):
    event_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type': 'date',
                'class': 'form-control',
                'min': datetime.date.today().isoformat(),
            }
        ),
        label='Event Date'
    )

    class Meta:
        model = Booking
        fields = ['name', 'phone', 'email', 'event_type', 'event_date', 'location', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Full Name',
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '+91 92350 54005',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'your@email.com',
            }),
            'event_type': forms.Select(attrs={
                'class': 'form-control form-select',
            }),
            'location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Venue / City / Address',
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Any special requests, preferences, or questions...',
            }),
        }
        labels = {
            'name': 'Full Name',
            'phone': 'Phone Number',
            'email': 'Email Address',
            'event_type': 'Type of Event',
            'event_date': 'Event Date',
            'location': 'Event Location',
            'message': 'Message / Special Requests',
        }

    def clean_event_date(self):
        date = self.cleaned_data.get('event_date')
        if date and date < datetime.date.today():
            raise forms.ValidationError("Event date cannot be in the past.")
        return date

    def clean_phone(self):
        phone = self.cleaned_data.get('phone', '').strip()
        digits = ''.join(c for c in phone if c.isdigit())
        if len(digits) < 9 or len(digits) > 15:
            raise forms.ValidationError("Enter a valid phone number (9–15 digits).")
        return phone


class ServiceReviewForm(forms.ModelForm):
    rating = forms.ChoiceField(
        choices=[(5, '5 - Excellent'), (4, '4 - Very Good'), (3, '3 - Good'), (2, '2 - Fair'), (1, '1 - Needs Improvement')],
        widget=forms.Select(attrs={'class': 'form-control form-select'}),
    )

    class Meta:
        model = ServiceReview
        fields = ['name', 'service_type', 'rating', 'review', 'location']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your name',
            }),
            'service_type': forms.Select(attrs={
                'class': 'form-control form-select',
            }),
            'review': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Tell visitors what you liked about the service...',
            }),
            'location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'City / Location (optional)',
            }),
        }
        labels = {
            'name': 'Your Name',
            'service_type': 'Service You Used',
            'rating': 'Rating',
            'review': 'Your Review',
            'location': 'Location',
        }
