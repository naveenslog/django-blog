from rest_framework import serializers
from .models import Post
from common.models import Category
from common.serializers import CategorySerializer

class PostSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True, many=True)
    
    class Meta:
        model = Post
        fields = "__all__"