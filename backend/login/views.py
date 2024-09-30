from rest_framework import serializers
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.db import IntegrityError
from . import serializer
from django.utils import timezone
from django.http import HttpResponse

def login(request):
    return 
    
def signup(request):
    return 

def logout(request):
    return 

def test_token(request):
    return 

def emergency_logout(request):
    return 