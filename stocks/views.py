from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from users.models import User
from .models import Give


def Dons(request):
    dons = Give.objects.all()
    return render(request, 'dons.html', context={"dons": dons})
