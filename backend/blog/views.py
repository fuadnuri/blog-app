from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from blog.models import Post,Comment
from blogapi.blogserializer import UserSerializer
class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {"message" : "hello world!"}
        return Response(content)

class AdminView(APIView):
    def get(self, request, format=None):
        user = User.objects.all()
        serializer = UserSerializer(user, many=True,context={'request': request})
        return Response(serializer.data)
    