from django.urls import path
from rest_framework import routers

from .views import PostApiView, LikeApiView, AnalyticView, UserActivityView

router = routers.SimpleRouter()
router.register(r'posts', PostApiView)
router.register(r'likes', LikeApiView)

urlpatterns = [
    path('analytics/', AnalyticView.as_view(), name='analytic'),
    path('user-activity/<int:pk>/', UserActivityView.as_view(), name='user-detail'),

]

urlpatterns += router.urls