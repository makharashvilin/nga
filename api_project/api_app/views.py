from django.core.serializers import serialize
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post
from .serializer import PostSerializer
from rest_framework import status




@api_view(['GET', 'POST'])
def index(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            post = serializer.save()
            return Response(
                {"message": "posti წარმატებით შექმნილია!", "post": PostSerializer(post).data},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


