from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

class Tag(models.Model):
    name = models.CharField(max_length=50)
    tags_created_on = models.DateTimeField(auto_now_add=True)
    tags_created_by = models.ForeignKey(User, related_name="created%(app_label)s_%(class)s_related", on_delete=models.CASCADE)
    tags_updated_on = models.DateTimeField(auto_now=True)
    tags_updated_by = models.ForeignKey(User, related_name="updated%(app_label)s_%(class)s_related", on_delete=models.CASCADE)
    tags_is_active = models.BooleanField(default=True)
    def __str__(self):
        return f"Tag: {self.name}"


class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    blogs_created_on = models.DateTimeField(auto_now_add=True)
    blogs_created_by = models.ForeignKey(User, related_name="created%(app_label)s_%(class)s_related", on_delete=models.CASCADE)
    blogs_updated_on = models.DateTimeField(auto_now=True)
    blogs_updated_by = models.ForeignKey(User, related_name="updated%(app_label)s_%(class)s_related", on_delete=models.CASCADE)
    blogs_is_active = models.BooleanField(default=True)