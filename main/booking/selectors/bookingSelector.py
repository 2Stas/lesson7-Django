
from main.models import Booking


def get_all_bookings():
    return Booking.objects.select_related('user', 'event').all()


def get_booking_by_id(booking_id):
    return Booking.objects.select_related('user','event' ).filter(id=booking_id).first()


def get_user_bookings(user_id):
    return Booking.objects.filter(user_id=user_id).select_related('event')


def get_event_bookings(event_id):
    return Booking.objects.filter(event_id=event_id).select_related('user')


def get_active_bookings():
    return Booking.objects.filter(status=Booking.Status.ACTIVE ).select_related('user', 'event')


def get_user_booking_for_event(user_id, event_id):
    return Booking.objects.filter(user_id=user_id, event_id=event_id ).first()
