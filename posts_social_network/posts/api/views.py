from django.contrib.auth import get_user_model
from django.db.models import Count

from django_filters import rest_framework as filters

from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from ..models import Post, Like
from .filters import DateRangeFilterSet
from .serializers import PostSerializer, AnalyticSerializer, UserSerializer, LikeSerializer

User = get_user_model()


class PostApiView(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin,  GenericViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get_queryset(self):
        queryset = Post.objects.all().annotate(total_likes=Count('like'))
        return queryset


class LikeApiView(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.CreateModelMixin,
                  mixins.DestroyModelMixin,
                  GenericViewSet):
    serializer_class = LikeSerializer
    queryset = Like.objects.all()


class AnalyticView(ListAPIView):
    queryset = Like.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = DateRangeFilterSet
    serializer_class = AnalyticSerializer

    def get_queryset(self):
        queryset = Like.objects.values('created_at').annotate(total_likes=Count('id'))
        filtered_queryset = self.filter_queryset(queryset)
        return filtered_queryset


class UserDetailView(RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()