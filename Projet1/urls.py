from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from Projet1 import settings
from blog.views import index
from stocks.views import Dons
from users.views import user, entr

urlpatterns = [
                  path('dons/', Dons, name='Dons'),
                  path('admin/', admin.site.urls),
                  path('', index, name='index'),
                  path('user/<str:slug>', user, name='user'),
                  path('entr/<str:slug>', entr, name='entr'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
