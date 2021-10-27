from django.shortcuts import render, HttpResponse
from .models import Post, Tag, Category
from config.models import SideBar
from django.views.generic import ListView, DetailView, TemplateView
from comment.models import Comment
from comment.forms import CommentForm
from django.shortcuts import get_object_or_404
from django.db.models import Q, F


# Create your views here.
class CommonViewMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'sidebars': SideBar.get_all()
        })
        context.update(Category.get_navs())
        # print("in CommonViewMixin:", context)
        return context


class IndexView(CommonViewMixin, ListView):
    queryset = Post.latest_posts()
    template_name = 'blog/list.html'
    context_object_name = 'post_list'
    paginate_by = 5
    # print("in IndexView")


class AuthorView(IndexView):
    def get_queryset(self):
        queryset = super(AuthorView, self).get_queryset()
        author_id = self.kwargs.get("author_id")
        return queryset.filter(owner_id=author_id)


class SearchView(IndexView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'keyword': self.request.GET.get('keyword', '')
        })
        return context

    def get_queryset(self):
        qs = super().get_queryset()
        keyword = self.request.GET.get('keyword')
        if not keyword:
            return qs
        return qs.filter(Q(title__icontains=keyword) | Q(desc__icontains=keyword))


class CategoryView(IndexView):
    def get_content_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_id = self.kwargs.get('category_id')
        category = get_object_or_404(Category, pk=category_id)
        context.update({
            'category': category
        })
        return context

    def get_queryset(self):
        qs = super().get_queryset()
        category_id = self.kwargs.get('category_id')
        return qs.filter(category_id=category_id)


class TagView(IndexView):
    def get_content_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag_id = self.kwargs.get('tag_id')
        tag = get_object_or_404(Tag, pk=tag_id)
        context.update({
            'tag': tag
        })
        return context

    def get_queryset(self):
        qs = super().get_queryset()
        tag_id = self.kwargs.get('tag_id')
        return qs.filter(tag__id=tag_id)


class PostDetailView(CommonViewMixin, DetailView):
    queryset = Post.latest_posts()
    template_name = 'blog/detail.html'
    context_object_name = 'post'
    pk_url_kwarg = 'post_id'

    def get(self, request, *args, **kwargs):
        response = super(PostDetailView, self).get(request, *args, **kwargs)
        self.handle_visited()
        return response

    def handle_visited(self):
        pv_increase = False
        uv_increase = False
        import datetime
        from django.core.cache import cache
        pv_key = 'pv:%s:%s'.format(self.request.uid, self.request.path)
        uv_key = 'uv:%s:%s:%s'.format(self.request.uid, str(datetime.date.today()), self.request.path)
        if not cache.get(pv_key):
            pv_increase = True
            cache.set(pv_key, 1, 1*60)
        if not cache.get(uv_key):
            uv_increase = True
            cache.set(uv_key, 1, 60*60*24)
        if pv_increase and uv_increase:
            Post.objects.filter(pk=self.object.id).update(pv=F('pv')+1, uv=F('uv')+1)
        elif pv_increase:
            Post.objects.filter(pk=self.object.id).update(pv=F('pv')+1)
        elif uv_increase:
            Post.objects.filter(pk=self.object.id).update(uv=F('uv')+1)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data()
    #     context.update({
    #         'comment_form': CommentForm(),
    #         'comment_list': Comment.get_by_target(self.request.path)
    #     })
    #     # print("self.reqeust.path:", self.request.path)
    #     # print("context:", context.get('request'))
    #     return context
#
# def post_list(request, category_id=None, tag_id=None):
#     tag = None
#     category = None
#
#     if tag_id:
#         post_list, tag = Post.get_by_tag(tag_id)
#     elif category_id:
#         post_list, category = Post.get_by_category(category_id)
#     else:
#         post_list = Post.latest_posts()
#
#     context = {
#         'post_list': post_list,
#         'tag': tag,
#         'category': category,
#         'sidebars': SideBar.get_all()
#     }
#     context.update(Category.get_navs())
#     print("in post_list view context:", context)
#     return render(request, 'blog/list.html', context=context)
#
#
def post_detail(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        post = None

    context = {
        'post': post,
        'sidebars': SideBar.get_all()
    }
    context.update(Category.get_navs())
    return render(request, 'blog/detail.html', context=context)

