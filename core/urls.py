from django.contrib import admin
from django.urls import path
from gagafood.views import *
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

def trigger_error(request):
    division_by_zero = 1 / 0

urlpatterns = [
    path('admin/', admin.site.urls),
    path('authentication/', include('authentication.urls')),
    path('', include('gagafood.urls')),
    path('sentry-debug/', trigger_error),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
