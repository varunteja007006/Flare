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

SOMETHING_WENT_WRONG = "Something went wrong"
INVALID_TOKEN = "Invalid Token"
LOGIN_SUCCESS = "Logged in Successfully"

@api_view(["POST"])
def login(request):
    if request.data["email"] != "":
        user = get_object_or_404(User, email=request.data["email"])
    else:
        user = get_object_or_404(User, username=request.data["username"])
    if not user.check_password(request.data["password"]):
        return Response(
            {
                "detail": "Password does not match",
                "data": False,
            },
            status=status.HTTP_400_BAD_REQUEST,
        )
    try:
        user.last_login = timezone.now()  # Use timezone.now() for UTC awareness (optional)
        user.save()
        token = Token.objects.create(user=user)
        sz = serializer.UserSerializer(instance=user)
        return Response(
            {
                "detail": LOGIN_SUCCESS,
                "data": {
                    "id": sz.data["id"],
                    "username": sz.data["username"],
                    "email": sz.data["email"],
                    "token": token.key,
                },
            },
            status=status.HTTP_200_OK,
        )
    except Exception as e:
        try:
            token = Token.objects.get(user=user)
            token.delete()  # If user already has a token delete and generate a new one.
            user.last_login = timezone.now()  # Use timezone.now() for UTC awareness (optional)
            user.save()
            token = Token.objects.create(user=user)
            sz = serializer.UserSerializer(instance=user)
            return Response(
                {
                    "detail": LOGIN_SUCCESS,
                    "data": {
                        "id": sz.data["id"],
                        "username": sz.data["username"],
                        "email": sz.data["email"],
                        "token": token.key,
                    },
                },
                status=status.HTTP_200_OK,
            )
        except Token.DoesNotExist:
            return Response(
                {
                    "detail": INVALID_TOKEN,
                    "data": False,
                },
                status=status.HTTP_401_UNAUTHORIZED,
            )
        except Exception as e:
            return Response(
                {
                    "detail": "Failed to login",
                    "data": False,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

@api_view(["POST"])
def signup(request):
    sz = serializer.UserSerializer(data=request.data)
    try:
        if sz.is_valid():
            sz.save()
            user = User.objects.get(username=request.data["username"])
            user.set_password(request.data["password"])
            user.save()
            return Response(
                {
                    "detail": "Sign up Successful",
                    "data": {
                        "id": sz.data["id"],
                        "username": sz.data["username"],
                        "email": sz.data["email"],
                    },
                },
                status=status.HTTP_201_CREATED,
            )
    except IntegrityError:
        return Response(
            {
                "detail": "Email address or username already exists",
                "data": False,
            },
            status=status.HTTP_400_BAD_REQUEST,
        )
    except serializers.ValidationError as e:
        return Response(
            {
                "detail": "Email address or username already exists",
                "data": False,
            },
            status=status.HTTP_400_BAD_REQUEST,
        )
    return Response(
        {
            "detail": sz.errors,
            "data": False,
        },
        status=status.HTTP_400_BAD_REQUEST,
    )

@api_view(["POST"])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def logout(request):
    try:
        token = request.headers.get("Authorization").split(" ")[
            1
        ]  # Assuming a Token token
        token = Token.objects.get(key=token)
        token.delete()  # Delete the token
        return Response(
            {
            "detail": "Successfully logged out", 
            "data": True},
            status=status.HTTP_200_OK,
        )
    except Token.DoesNotExist:
        return Response(
            {
            "detail": "The token does not exist",
            "data": False},
            status=status.HTTP_401_UNAUTHORIZED,
        )
    except Exception as e:
        return Response(
            {
            "detail": f"{e}"
            ,"data": False},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

@api_view(["GET"])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request):
    return Response({
    "detail":f"passed for {request.user.email}", 
    "data": True, 
    "isAuthenticated": True}, 
    status=status.HTTP_200_OK,)

@api_view(["POST"])
def emergency_logout(request):
    try:
        tokens = Token.objects.all()
        tokens.delete()
        return Response(
            {
                "detail": "Logged out all the users",
                "data": True,
            },
            status=status.HTTP_200_OK,
        )
    except Exception as e:
        return Response(
            {
                "detail": f"{e}",
                "data": False,
            },
            status=status.HTTP_400_BAD_REQUEST,
        )