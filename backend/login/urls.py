from django.urls import path
from . import views
urlpatterns = [
    path("login", views.login),
    path("sign-up", views.signup),
    path("logout", views.logout),
    path("test-token", views.test_token),
    path("emergency-logout", views.emergency_logout),
]