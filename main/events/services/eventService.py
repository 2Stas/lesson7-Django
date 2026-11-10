
from main.models import Event


def create_event(title, description, category, organizer,
                 date, location, price=0):
    event = Event.objects.create(
        title=title,
        description=description,
        category=category,
        organizer=organizer,
        date=date,
        location=location,
        price=price
    )

    return event


def update_event(event_id, title, description, category,
                 date, location, price, status):
    event = Event.objects.filter(id=event_id).first()

    if event is None:
        return None

    event.title = title
    event.description = description
    event.category = category
    event.date = date
    event.location = location
    event.price = price
    event.status = status

    event.save()

    return event


def delete_event(event_id):
    event = Event.objects.filter(id=event_id).first()

    if event is None:
        return False

    event.delete()

    return True


def publish_event(event_id):
    event = Event.objects.filter(id=event_id).first()

    if event is None:
        return None

    event.status = Event.Status.PUBLISHED
    event.save()

    return event


def cancel_event(event_id):
    event = Event.objects.filter(id=event_id).first()

    if event is None:
        return None

    event.status = Event.Status.CANCELLED
    event.save()

    return event
