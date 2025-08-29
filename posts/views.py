from rest_framework import generics, status, mixins, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404
from .models import Post, Comment, Tag
from .serializers import PostListSerializer, PostDetailSerializer, CommentSerializer, TagSerializer
from .permissions import IsAuthorOrReadOnly
from .services import add_comment_to_post
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

class PostViewSet(viewsets.ModelViewSet):
  
    queryset = Post.objects.all().prefetch_related('comments', 'tags').select_related('author')
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['author__id', 'tags__name']
    search_fields = ['title', 'body', 'author__username', 'tags__name']
    ordering_fields = ['created_at', 'updated_at', 'title']

    def get_serializer_class(self):
        if self.action in ['list']:
            return PostListSerializer
        return PostDetailSerializer

    def perform_create(self, serializer):
        
        serializer.save()

    @action(detail=True, methods=['get'], permission_classes=[IsAuthenticatedOrReadOnly])
    def comments(self, request, pk=None):
        post = self.get_object()
        qs = post.comments.all()
        page = self.paginate_queryset(qs)
        serializer = CommentSerializer(page or qs, many=True)
        return self.get_paginated_response(serializer.data) if page is not None else Response(serializer.data)

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticatedOrReadOnly])
    def add_comment(self, request, pk=None):
        post = self.get_object()
        serializer = CommentSerializer(data=request.data)
       
        if serializer.is_valid():
            
            try:
                comment = add_comment_to_post(post, serializer.validated_data.get('author_name'), serializer.validated_data.get('body'))
            except ValueError as e:
                return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)
            out = CommentSerializer(comment)
            return Response(out.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentListView(generics.ListAPIView):
   
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        post_id = self.kwargs.get('post_pk') or self.kwargs.get('post_id') or self.kwargs.get('pk')
        return Comment.objects.filter(post__id=post_id)

class TagListCreateView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
