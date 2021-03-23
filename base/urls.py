from django.conf.urls.static import static
from django.conf.urls import url
from base import views
from django.conf import settings
from django.urls import path


urlpatterns = [   
     url(r'^dashboard/', views.dashboard_view, name='dashboard'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
