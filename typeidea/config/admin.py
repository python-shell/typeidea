from django.contrib import admin
from .models import Link, SideBar
from custom_site import custom_site
from base_admin import BaseOwnerAdmin

# Register your models here.
@admin.register(Link, site=custom_site)
class LinkAdmin(BaseOwnerAdmin):
    list_display = ['title', 'href', 'status', 'owner', 'created_time']
    fields = ['title', 'href', 'status', 'weight']


@admin.register(SideBar, site=custom_site)
class SidebarAdmin(BaseOwnerAdmin):
    list_display = ['title', 'display_type', 'content', 'status', 'created_time']
    fields = ['title', 'display_type', 'content']

