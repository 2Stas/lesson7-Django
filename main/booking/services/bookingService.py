
from main.models import Booking, Event


def create_booking(user, event):
    if event.status != Event.Status.PUBLISHED:
        return None

    existing_booking = Booking.objects.filter(
        user=user,
        event=event
    ).first()

    if existing_booking is not None:
        if existing_booking.status == Booking.Status.ACTIVE:
            return None

        existing_booking.status = Booking.Status.ACTIVE
        existing_booking.save()

        return existing_booking

    booking = Booking.objects.create(user=user, event=event )

    return booking


def cancel_booking(booking_id, user):
    booking = Booking.objects.filter(id=booking_id, user=user).first()

    if booking is None:
        return False

    if booking.status == Booking.Status.CANCELLED:
        return False

    booking.status = Booking.Status.CANCELLED
    booking.save()

    return True


def delete_booking(booking_id):
    booking = Booking.objects.filter(id=booking_id).first()

    if booking is None:
        return False

    booking.delete()

    return True
