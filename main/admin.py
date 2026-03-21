from django.contrib import admin
from .models import Booking, Testimonial, GalleryImage


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display  = ('name', 'phone', 'email', 'event_type', 'event_date', 'location', 'status', 'created_at')
    list_filter   = ('event_type', 'status', 'event_date')
    search_fields = ('name', 'phone', 'email', 'location')
    ordering      = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')
    list_per_page = 25
    date_hierarchy = 'event_date'

    fieldsets = (
        ('Customer Information', {
            'fields': ('name', 'phone', 'email')
        }),
        ('Event Details', {
            'fields': ('event_type', 'event_date', 'location', 'message')
        }),
        ('Status & Timestamps', {
            'fields': ('status', 'created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )

    actions = ['mark_confirmed', 'mark_completed', 'mark_cancelled']

    @admin.action(description='Mark selected bookings as Confirmed')
    def mark_confirmed(self, request, queryset):
        updated = queryset.update(status='confirmed')
        self.message_user(request, f'{updated} booking(s) marked as Confirmed.')

    @admin.action(description='Mark selected bookings as Completed')
    def mark_completed(self, request, queryset):
        updated = queryset.update(status='completed')
        self.message_user(request, f'{updated} booking(s) marked as Completed.')

    @admin.action(description='Mark selected bookings as Cancelled')
    def mark_cancelled(self, request, queryset):
        updated = queryset.update(status='cancelled')
        self.message_user(request, f'{updated} booking(s) marked as Cancelled.')


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display  = ('name', 'location', 'event_type', 'rating', 'is_active', 'created_at')
    list_filter   = ('is_active', 'rating')
    search_fields = ('name', 'event_type', 'message')
    list_editable = ('is_active',)
    ordering      = ('-created_at',)


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display  = ('title', 'category', 'order', 'is_active', 'created_at')
    list_filter   = ('category', 'is_active')
    search_fields = ('title', 'caption')
    list_editable = ('order', 'is_active')
    ordering      = ('order', '-created_at')
    

   
