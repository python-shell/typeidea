"""typeidea URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.sitemaps import views as sitemap_views
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls

from custom_site import custom_site
# from blog.views import post_list, post_detail
from blog.views import IndexView, CategoryView, TagView, PostDetailView, SearchView, AuthorView
from config.views import links, LinkView
from comment.views import CommentView
from blog.rss import LatestPostFeed
from blog.sitemap import BlogSitemap
# rest_framework
# from blog.apis import post_list, PostList
from blog.apis import PostViewSet, CategoryViewSet


router = DefaultRouter()
router.register(r'post', PostViewSet, base_name='api-post')
router.register(r'category', CategoryViewSet, base_name='api-category')
urlpatterns = [
    url(r'^$', IndexView.as_view(), name='post_list'),
    url(r'^category/(?P<category_id>\d+)/$', CategoryView.as_view(), name='category_list'),
    url(r'^tag/(?P<tag_id>\d+)/$', TagView.as_view(), name='tag_list'),
    url(r'^post/(?P<post_id>\d+).html$', PostDetailView.as_view(), name='post_detail'),
    url(r'^links/$', LinkView.as_view(), name='links'),

    url(r'^search/$', SearchView.as_view(), name='search'),
    url(r'^author_search/(?P<author_id>\d+)$', AuthorView.as_view(), name='author_search'),
    url(r'^comment/$', CommentView.as_view(), name='comment'),

    url(r'^ckeditor/', include('ckeditor_uploader.urls')),

    url(r'^rss|feed$', LatestPostFeed(), name='rss'),
    url(r'^sitemap\.xml$', sitemap_views.sitemap, {'sitemaps': {'posts': BlogSitemap}}),
    url(r'^super_admin/', admin.site.urls),
    url(r'^admin/', custom_site.urls),

    # url(r'^api/post/', post_list, name='post_list'),
    # url(r'^api/post/', PostList.as_view(), name='post_list')
    url(r'^api/', include(router.urls)),
    url(r'^api/docs/', include(include_docs_urls(title='typeidea docs')))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns


if settings.DEBUG:
    urlpatterns += [
        url(r'^silk/', include('silk.urls', namespace='silk')),
    ]