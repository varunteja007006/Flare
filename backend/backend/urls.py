
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include("login.urls")),
    path('api/home/', include("home.urls")),
    path('api/sentiment_analysis/', include("sentiment_analysis.urls")),
    path('api/products/', include("products.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)