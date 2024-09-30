from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from . import models
from feedback.serializers import FeedbackSerializer

# Create your views here.
@csrf_exempt
def feedback(request):
    # Post request handled here
    if request.method == "POST":
        data = JSONParser().parse(request)
        serializer = FeedbackSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    # get request handled here
    elif request.method == "GET":
        feedback = models.Feedback.objects.all()
        serializer = FeedbackSerializer(feedback, many=True)
        return JsonResponse(serializer.data, safe=False)
