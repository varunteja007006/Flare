from rest_framework import serializers
from . import models
from sentiment_analysis.sentiment_analysis import sentiment_analysis

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Feedback
        fields = ["name", "email", "feedback"]
        read_only_fields = ['sentiment_polarity']  # sentiment_polarity is not provided in request
    
    def create(self, validated_data):
        # Compute sentiment polarity based on feedback content
        feedback_content = validated_data.get('feedback')
        validated_data['sentiment_polarity'] = sentiment_analysis(feedback_content)
        return super().create(validated_data)
    
class GetFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Feedback
        fields = '__all__'

class GetNoAuthFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Feedback
        fields = ["id", "name", "feedback", "sentiment_polarity"]