
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include('api.urls')),
    path('apicrud/', include('apicrud.urls')),

    path('seller/', include('sellerDashboard.urls')),
    path('manager/', include('superDashboard.urls')),

    path('', include('frontend.urls')),
]

# media
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
