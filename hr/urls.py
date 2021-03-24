from django.conf.urls.static import static 
from django.conf.urls import url
from django.urls import path
from hr import views
from django.conf import settings

urlpatterns = [   
    path('', views.hr, name='hr')
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
