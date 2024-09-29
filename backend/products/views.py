from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
from .models import Product, Variant, Category
from .serializer import CategorySerializer

@api_view(["GET"])
def get_category(request):
    try:
        category = Category.objects.all().order_by("-created_on").values()
        serializer = CategorySerializer(category, many=True)
        return Response({ 
            "detail": "Success" ,"data":serializer.data
            }, 
            status=status.HTTP_200_OK)
    except Exception as e:
        return Response(
            {
                "detail": f"{e}",
                "data": False,
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

@api_view(["GET"])
def get_variants(request):
    variants = Variant.objects.all()
    return