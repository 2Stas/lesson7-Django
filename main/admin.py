
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Category, Event, Booking


@admin.register(User)
class CustomUserAdmin(UserAdmin):

    list_display = ('username', 'email', 'first_name', 'last_name', 'role', 'is_active')

    list_filter = ('role', 'is_active', 'is_staff')

    search_fields = ('username', 'email', 'first_name', 'last_name')

    fieldsets = UserAdmin.fieldsets + (
        ('Additional Information', {
            'fields': ('role',)
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Information', {
            'fields': ('role',)
        }),
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ('name', 'description')

    search_fields = ('name',)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):

    list_display = ('title', 'category', 'organizer', 'date', 'price', 'status')

    list_filter = ('status', 'category', 'date')

    search_fields = ('title', 'description', 'location')

    ordering = ('date',)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):

    list_display = ('user', 'event', 'booking_date', 'status')

    list_filter = ('status', 'booking_date')

    search_fields = ('user__username', 'event__title')

    ordering = ('-booking_date',)
