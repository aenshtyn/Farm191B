from django.conf.urls.static import static
from django.conf.urls import url
from base import views
from django.conf import settings
from django.urls import path


urlpatterns = [   
     path('', views.pie_chart, name='piechart'),
     path('index', views.index, name = 'index'),
     path('morning_milk/', views.morning_milk_production, name='morning-milk-production'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

