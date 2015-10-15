from django.conf.urls import patterns, url
from django.conf import settings
from django.conf.urls.static import static

from website import views

urlpatterns = patterns(
    '',
    url(r'^$', views.home, name='home'),
    url(r'^galerie$', views.galerie, name='galerie'),
    url(r'^prestation', views.prestation, name='prestation'),
    url(r'^map', views.map, name='map'),
    )+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)