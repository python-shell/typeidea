
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAdminUser
# from django.urls import reverse
# from rest_framework import reverse
from .models import Post, Category
from .serializers import PostSerializer, PostDetailSerializer, CategorySerializer, CategoryDetailSerializer
from utils.my_pagenation import CustomPagination


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.filter(status=Category.STATUS_NORMAL)
    serializer_class = CategorySerializer
    
    # def retrieve(self, request, *args, **kwargs):
    #     self.serializer_class = CategoryDetailSerializer
    #     return super(CategoryViewSet, self).retrieve(request, *args, **kwargs)


class PostViewSet(viewsets.ModelViewSet):
    """
        django rest framework viewset
    """
    # print(reverse('api:post-list'))
    queryset = Post.objects.filter(status=Post.STATUS_NORMAL)
    serializer_class = PostSerializer
    pagination_class = CustomPagination
    # lookup_url_kwarg = 'my_cate'
    # permission_classes = [IsAdminUser]

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = PostDetailSerializer
        return super(PostViewSet, self).retrieve(request, *args, **kwargs)

    def filter_queryset(self, queryset):
        category_id = self.request.query_params.get('category')
        if category_id:
            queryset = queryset.filter(category_id=category_id, status=Post.STATUS_NORMAL)
        return queryset
