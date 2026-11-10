
from django.contrib.auth import get_user_model


User = get_user_model()


def get_user_by_id(user_id):
    return User.objects.filter(id=user_id).first()


def get_user_by_username(username):
    return User.objects.filter(username=username).first()


def get_all_users():
    return User.objects.all()
