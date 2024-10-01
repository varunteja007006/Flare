from django.urls import path, include
from . import views 

urlpatterns = [
    path("", views.feedback, name="feedback"),
    path("get-feedback", views.get_feedback, name="get_feedback"),
]