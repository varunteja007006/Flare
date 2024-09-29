from django.contrib import admin
from .models import Blog, Tag, Author

admin.site.site_header = "Blogs Admin"

class BlogsAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'blogs_created_on']

admin.site.register(Blog, BlogsAdmin)

class TagAdmin(admin.ModelAdmin):
    list_display = ['name',  'tags_created_on']

admin.site.register(Tag, TagAdmin)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['user']

admin.site.register(Author, AuthorAdmin)