from django.contrib import admin
from .models import Category, Tag, Post
from django.utils.html import format_html
from django.urls import reverse
from .adminforms import PostAdminForm
from custom_site import custom_site
from django.contrib.auth.models import User
from django.contrib.auth import get_permission_codename
from base_admin import BaseOwnerAdmin
from django.core.exceptions import FieldError
#日志记录模块
from django.contrib.admin.models import LogEntry
# Register your models here.


@admin.register(LogEntry, site=custom_site)
class LogEntryAdmin(admin.ModelAdmin):
    list_display = ['user', 'object_repr', 'object_id', 'action_flag', 'action_time', 'change_message']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        try:
            res = qs.filter(owner=request.user)
        except FieldError:
            res = qs.filter(user=request.user)
        return res


class PostInline(admin.TabularInline):
    fields = ('title', 'desc', 'owner')
    # extra = 2
    model = Post


@admin.register(Category, site=custom_site)
class CategoryAdmin(BaseOwnerAdmin):
    inlines = (PostInline, )
    list_display = ('name', 'status', 'is_nav', 'owner', 'created_time')
    fields = ('name', 'status', 'is_nav', 'owner')


@admin.register(Tag, site=custom_site)
class TagAdmin(BaseOwnerAdmin):
    list_display = ('name', 'status', 'created_time')
    fields = ('name', 'status')


class CategoryOwnerFilter(admin.SimpleListFilter):
    """
        自定义过滤器只展示当前用户分类
    """
    title = '分类过滤器'
    # Human-readable title to appear in the right sidebar.
    parameter_name = 'owner_category'  #URL后面的查询参数自定义 http://192.168.0.106:8000/admin/blog/post/?owner_category1=3&q=

    def lookups(self, request, model_admin):
        return Category.objects.filter(owner=request.user).values_list("id", "name")

    def queryset(self, request, queryset):
        category_id = self.value()
        if category_id:
            return queryset.filter(category_id=category_id)
        return queryset


@admin.register(Post, site=custom_site)
class PostAdmin(BaseOwnerAdmin):
    form = PostAdminForm
    list_display = ['title', 'category', 'status',
                    'created_time', 'owner', 'operator']
    list_display_links = []
    list_filter = [CategoryOwnerFilter]
    search_fields = ['title', 'category__name']

    actions_on_top = True
    actions_on_bottom = True

    save_on_top = True
    exclude = ['owner']
    fieldsets = (
        ('基础配置', {
            'description': '基础配置描述',
            'fields': (
                ('title', 'category'),
                'status',
            )
        }),
        ('内容', {
            'fields': (
                'desc',
                'content'
            )
        }),
        ('额外配置', {
            'classes': 'wide',
            'fields': (
                'tag',
            )
        }),
    )

    filter_horizontal = ('tag', )
    # fields = [
    #     ('category', 'title'),
    #     'desc',
    #     'status',
    #     'content',
    #     'tag',
    #     # 'owner',
    # ]

    def operator(self, obj):
        return format_html('<a href="{}">编辑</a>',
                           reverse('cus_admin:blog_post_change', args=(obj.id, )))
    operator.short_description = '操作'

    # class Media:
    #     css = {
    #         'all': ("https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css", ),
    #     }
    #     js = ('https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/js/bootstrap.bundle.js', )
    def has_add_permission(self, request):
        print("in has add permission")
        print("self.opts:", self.opts)  # blog.post
        opts = self.opts
        codename = get_permission_codename('add', opts)
        print(opts.app_label, codename)
        return request.user.has_perm("%s.%s" % (opts.app_label, codename))


