from django.urls import path
from . import views

urlpatterns = [
    path('get_variants',  views.get_variants),
    path('get_category', views.get_category),
]