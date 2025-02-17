from django.contrib.auth import get_user_model
from rest_framework import viewsets
from .models import Post
from .permissions import IsAuthorOrReadOnly  # استيراد الصلاحية الجديدة
from .serializers import PostSerializer, UserSerializer


class PostViewSet(viewsets.ModelViewSet):  # بدلاً من عدة Views
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
