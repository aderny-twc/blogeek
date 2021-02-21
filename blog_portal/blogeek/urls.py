from django.urls import path
from .views import add_posts, HomeBlogPosts, BlogPostsByCategory, ViewBlogPosts

urlpatterns = [
    path('', HomeBlogPosts.as_view(), name='home'),
    path('category/<int:category_id>/', BlogPostsByCategory.as_view(), name='category'),
    path('posts/<int:pk>/', ViewBlogPosts.as_view(), name='view_blogposts'),
    path('posts/add-posts/', add_posts, name='add-posts'),
]