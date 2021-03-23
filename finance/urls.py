from django.conf.urls.static import static
from django.conf.urls import url
from finance import views
from django.conf import settings
from django.urls import path

urlpatterns = [
        url(r'^finance$', views.home, name='finance'),
    ]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
