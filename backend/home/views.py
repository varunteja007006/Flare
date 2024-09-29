from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
from .serializer import FeedbackSerializer
from .models import Feedback
from sentiment_analysis.sentiment_analysis import sentiment_analysis

# Create your views here.
@api_view(["POST"])
def post_feedback(request):
    serializer = FeedbackSerializer(data=request.data)
    feedback = request.data["feedback"]
    sentiment = sentiment_analysis(feedback)
    print(sentiment)
    try:
        if serializer.is_valid():
            validated_data = serializer.validated_data  # Access validated data
            validated_data['sentiment'] = sentiment
            serializer.save()
            return Response({ "detail": "Feedback Submitted" ,"data":serializer.data}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response(
            {
                "detail": f"{e}",
                "data": False,
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

@api_view(["GET"])
def get_feedback(request):
    try:
        feedbacks = Feedback.objects.all().order_by("-created_date").values()
        serializer = FeedbackSerializer(feedbacks, many=True)
        return Response({ "detail": "Success" ,"data":serializer.data}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(
            {
                "detail": f"{e}",
                "data": False,
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

