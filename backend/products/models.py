from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, related_name='created_product_category_%(app_label)s_%(class)s_related', on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, related_name='updated_product_category_%(app_label)s_%(class)s_related', on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return self.name

class Variant(models.Model):
    name = models.CharField(max_length=50, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, related_name='created_product_variant_%(app_label)s_%(class)s_related', on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, related_name='updated_product_variant_%(app_label)s_%(class)s_related', on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    variant = models.ManyToManyField(Variant)
    features = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, related_name='created_product_%(app_label)s_%(class)s_related', on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, related_name='updated_product_%(app_label)s_%(class)s_related', on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return self.name
