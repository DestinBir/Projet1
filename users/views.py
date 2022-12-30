from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from users.models import User, Entr


def user(request, slug):
    current_user = get_object_or_404(User, name=slug)
    return render(request, 'user.html', context={"user": current_user})


def entr(request, slug):
    current_entr = get_object_or_404(Entr, name=slug)
    return render(request, 'entr.html', context={"entr": current_entr})
