from django.urls import path
from . import views

urlpatterns = [
    path('', views.user),
    path('signIn/',  views.signIn)
]