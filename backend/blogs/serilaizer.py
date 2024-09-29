from rest_framework import serializers
from .models import Blog, Tag, Author

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name', 'created_at', 'created_by', 'updated_on', 'updated_by']

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['user']

class BlogSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Blog
        fields = ['title', 'content', 'author', 'tags', 'created_at', 'created_by', 'updated_on', 'updated_by']