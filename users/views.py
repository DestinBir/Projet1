from django.shortcuts import render
from django.http import HttpResponse

def signIn(request):
    
    return HttpResponse("Inscription")

def user(request):

    return HttpResponse("Je suis un utilistaeur")