from . import models
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from feedback.serializers import FeedbackSerializer, GetNoAuthFeedbackSerializer
from sentiment_analysis.sentiment_analysis import sentiment_analysis
# Create your views here.

@api_view(['POST', 'GET'])
def feedback(request):
    if request.method == 'POST':
        # add sentiment polarity
        request.data["sentiment_polarity"] = sentiment_analysis(request.data["feedback"])
        serializer = FeedbackSerializer(data=request.data)
        # validate data & save
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        feedback = models.Feedback.objects.values('id','name', 'feedback', 'sentiment_polarity')
        serializer = GetNoAuthFeedbackSerializer(feedback, many=True)
        return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated, IsAdminUser])
def get_feedback(request):
    feedback = models.Feedback.objects.all()
    serializer = FeedbackSerializer(feedback, many=True)
    return Response(serializer.data)
