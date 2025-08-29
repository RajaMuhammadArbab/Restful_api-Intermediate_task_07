
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentListView, TagListCreateView

router = DefaultRouter()
router.register(r'', PostViewSet, basename='post')

urlpatterns = [
    path('', include(router.urls)),
    
    path('<int:post_pk>/comments/', CommentListView.as_view(), name='post-comments'),
   
    path('tags/', TagListCreateView.as_view(), name='tag-list-create'),
]
