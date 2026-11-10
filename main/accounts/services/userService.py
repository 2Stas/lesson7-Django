
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model


User = get_user_model()


def register_user(username, email, password, first_name='', last_name=''):
    user = User.objects.create_user(
        username=username,
        email=email,
        password=password,
        first_name=first_name,
        last_name=last_name
    )

    return user


def login_user(request, username, password):
    user = authenticate(request, username=username, password=password )

    if user is not None:
        login(request, user)

    return user


def logout_user(request):
    logout(request)
