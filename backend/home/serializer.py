from rest_framework import serializers
from .models import Feedback

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'phone_number', 'feedback','created_date']