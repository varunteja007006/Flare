from . import models
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from feedback.serializers import FeedbackSerializer, GetNoAuthFeedbackSerializer, GetFeedbackSerializer
from drf_yasg.utils import swagger_auto_schema

@swagger_auto_schema(method='get', tags=['Feedback'], operation_description="Get feedback list", responses={200: GetNoAuthFeedbackSerializer(many=True)})   
@swagger_auto_schema(method='post', tags=['Feedback'], operation_description="Submit feedback", request_body=FeedbackSerializer)   
@api_view(['POST', 'GET'])
def feedback(request):
    if request.method == 'POST':
        serializer = FeedbackSerializer(data=request.data)
        # validate data & save
        if serializer.is_valid():
            serializer.save()
            return Response({'success': True}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        feedback = models.Feedback.objects.values('id','name', 'feedback', 'sentiment_polarity')
        serializer = GetNoAuthFeedbackSerializer(feedback, many=True)
        return Response(serializer.data)

@swagger_auto_schema(method='get', tags=['Feedback'], operation_description="Get feedback list for admins", responses={200: GetFeedbackSerializer(many=True)}) 
@api_view(['GET'])
@permission_classes([IsAuthenticated, IsAdminUser])
def get_feedback(request):
    feedback = models.Feedback.objects.all()
    serializer = GetFeedbackSerializer(feedback, many=True)
    return Response(serializer.data)
