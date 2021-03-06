from django.db.models import Count

from django_filters import rest_framework as filters

from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import AllowAny

from ..models import Post, Like, UserProfile
from .filters import DateRangeFilterSet
from .serializers import PostSerializer, AnalyticSerializer, UserSerializer, LikeSerializer, UserSignUpSerializer


class PostApiViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin,  GenericViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get_queryset(self):
        queryset = Post.objects.all().annotate(total_likes=Count('like'))
        return queryset


class LikeApiViewSet(mixins.ListModelMixin,
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
        queryset = Like.objects.values('created_at').annotate(total_likes=Count('pk'))
        filtered_queryset = self.filter_queryset(queryset)
        return filtered_queryset


class UserActivityView(RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = UserProfile.objects.all()


class SignUpUserViewSet(mixins.CreateModelMixin, GenericViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserSignUpSerializer
    permission_classes = [AllowAny]

