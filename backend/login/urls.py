from django.urls import path
from . import views
urlpatterns = [
    path("login", views.login, name="login"),
    path("sign-up", views.signup, name="signup"),
    path("logout", views.logout, name="logout"),
    path("test-token", views.test_token, name="test_token"),
    path("emergency-logout", views.emergency_logout, name="emergency_logout"),
]