from django.urls import path
from rest_framework import routers

from .views import PostApiViewSet, LikeApiViewSet, AnalyticView, UserActivityView, SignUpUserViewSet

router = routers.SimpleRouter()
router.register(r'posts', PostApiViewSet)
router.register(r'likes', LikeApiViewSet)
router.register(r'sign-up', SignUpUserViewSet)

urlpatterns = [
    path('analytics/', AnalyticView.as_view(), name='analytic'),
    path('user-activity/<int:pk>/', UserActivityView.as_view(), name='user-activity'),

]

urlpatterns += router.urls