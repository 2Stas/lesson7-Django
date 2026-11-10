
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser):

    class Role(models.TextChoices):
        USER = 'user'
        ADMIN = 'admin'
        MODERATOR = 'moderator'

    role = models.CharField( max_length=20, choices=Role.choices, default=Role.USER)

    def __str__(self):
        return self.username


class Category(models.Model):

    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Event(models.Model):

    class Status(models.TextChoices):
        DRAFT = 'draft'
        PUBLISHED = 'published'
        CANCELLED = 'cancelled'

    title = models.CharField(max_length=200)
    description = models.TextField()

    category = models.ForeignKey( Category, on_delete=models.PROTECT, related_name='events')

    organizer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='organized_events')

    date = models.DateTimeField()
    location = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    status = models.CharField(max_length=20, choices=Status.choices, default=Status.DRAFT)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['date']
        verbose_name = 'Event'
        verbose_name_plural = 'Events'

    def __str__(self):
        return self.title


class Booking(models.Model):

    class Status(models.TextChoices):
        ACTIVE = 'active'
        CANCELLED = 'cancelled'

    user = models.ForeignKey( settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='bookings')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='bookings')

    booking_date = models.DateTimeField(auto_now_add=True)

    status = models.CharField(max_length=20, choices=Status.choices, default=Status.ACTIVE)

    class Meta:
        ordering = ['-booking_date']
        verbose_name = 'Booking'
        verbose_name_plural = 'Bookings'

        constraints = [
            models.UniqueConstraint(fields=['user', 'event'], name='unique_user_event_booking')
        ]

    def __str__(self):
        return f'{self.user.username} - {self.event.title}'
