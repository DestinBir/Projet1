from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from users.models import User


def signIn(request):
    return HttpResponse("Inscription")


def user(request, slug):
    current_user = get_object_or_404(User, name=slug)
    return HttpResponse('je suis '+f'{current_user.name} {current_user.email}')
