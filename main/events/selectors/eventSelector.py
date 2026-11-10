
from main.models import Event


def get_all_events():
    return Event.objects.select_related('category','organizer').all()


def get_event_by_id(event_id):
    return Event.objects.select_related( 'category', 'organizer').filter(id=event_id).first()


def get_events_by_category(category_id):
    return Event.objects.filter(category_id=category_id)


def get_events_by_status(status):
    return Event.objects.filter(status=status)


def get_events_by_organizer(organizer_id):
    return Event.objects.filter(organizer_id=organizer_id)


def get_published_events():
    return Event.objects.filter(status=Event.Status.PUBLISHED).select_related('category', 'organizer')


def search_events(query):
    return Event.objects.filter(title__icontains=query).select_related('category', 'organizer')
