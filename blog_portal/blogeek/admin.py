from django.contrib import admin
from .models import BlogPosts, Category


class BlogPostsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'created_at', 'updated_at', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'category')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.register(BlogPosts, BlogPostsAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.site_title = 'Управление статьями'
admin.site.site_header = 'Управление статьями'
