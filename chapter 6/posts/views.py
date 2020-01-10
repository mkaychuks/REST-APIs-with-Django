from rest_framework import generics
# from rest_framework.permissions import IsAuthenticated


from .models import Post
from .serializers import PostSerializer
from .permissions import IsAuthorOrReadOnly  # custom permission class


class PostList(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.order_by('-created_at')


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
