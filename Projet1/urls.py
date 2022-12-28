from django.contrib import admin
from django.urls import path, include

from blog.views import index
from users.views import user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('user/<str:slug>', user, name='user'),
]
