from django.urls import include,path
from django.conf.urls.static import static
from django.conf.urls import url
from django.conf import settings
from rest_framework import routers
from API.views import LedgerViewSet

router = routers.DefaultRouter()
router.register(r'ledger', LedgerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
