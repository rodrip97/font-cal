from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from .views import *


urlpatterns = [

    url('admin/', admin.site.urls),
    url(r'^$', index, name='index'),
    url('about', about, name='about'),
    url('portfolio', portfolio, name='portfolio'),
    url('contact', contact, name='contact'),
    url('calendar', calendar, name='calendar'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
