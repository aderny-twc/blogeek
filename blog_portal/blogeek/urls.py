from django.urls import path
from .views import view_blogposts, add_posts, HomeBlogPosts, BlogPostsByCategory

urlpatterns = [
    path('', HomeBlogPosts.as_view(), name='home'),
    path('category/<int:category_id>/', BlogPostsByCategory.as_view(), name='category'),
    path('posts/<int:blogposts_id>/', view_blogposts, name='view_blogposts'),
    path('posts/add-posts/', add_posts, name='add-posts'),
]