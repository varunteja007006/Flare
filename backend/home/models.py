from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Feedback(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=254)
    phone_number = PhoneNumberField(blank=True)
    feedback = models.TextField()
    sentiment = models.IntegerField(blank=True, null=True, default=0)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Feedbacks'

    def __str__(self):
        return self.name