from django.db import models

# Create your models here.
class Feedback(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    feedback = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

