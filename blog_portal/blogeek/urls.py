from django.urls import path
from .views import HomeBlogPosts, BlogPostsByCategory, ViewBlogPosts, CreateBlogPosts

urlpatterns = [
    path('', HomeBlogPosts.as_view(), name='home'),
    path('category/<int:category_id>/', BlogPostsByCategory.as_view(), name='category'),
    path('posts/<int:pk>/', ViewBlogPosts.as_view(), name='view_blogposts'),
    path('posts/add-posts/', CreateBlogPosts.as_view(), name='add-posts'),
]