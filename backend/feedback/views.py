from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from . import models
from feedback.serializers import FeedbackSerializer

# Create your views here.
@csrf_exempt
def feedback(request):
    if request.method == "POST":
        return
    if request.method == "GET":
        feedback = models.Feedback.objects.all()
        serializer = FeedbackSerializer(feedback, many=True)
        return JsonResponse(serializer.data, safe=False)
