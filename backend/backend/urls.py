
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include("login.urls")),
    path('api/v1/feedback/', include("feedback.urls")),
    path('api/v1/login/', include("login.urls")),
    path('api/v1/sentiment_analysis/', include("sentiment_analysis.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)