from django.contrib import admin
from .models import Product,Variant,Category

# Register your models here.
admin.site.site_header = "Products Admin"

admin.site.register(Product)
admin.site.register(Variant)
admin.site.register(Category)