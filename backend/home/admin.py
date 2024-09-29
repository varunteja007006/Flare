from django.contrib import admin
from .models import Feedback

admin.site.site_header = "Home Admin"

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email','created_date')

admin.site.register(Feedback, FeedbackAdmin)