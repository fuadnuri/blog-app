from rest_framework import serializers
from blog.models import Post, Comment
from userProfile.models import Profile

from django.contrib.auth.models import User


class ProfileSerializer(serializers.Serializer):
    class Meta:
        model = Profile 
        fields = (
            'avater'
        )
class UserSerializer(serializers.Serializer):
    avater = ProfileSerializer(many=False,read_only=True)
    class Meta:
        model = User
        fields = (
            'Username',
            'avatar'
        )

class CommentSerializer(serializers.Serializer):
    pass
    
class PostSerializer(serializers.Serializer):
    pass



