from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView

from .forms import PostsForm
from .models import BlogPosts, Category


class HomeBlogPosts(ListView):
    model = BlogPosts
    template_name = 'blogeek/home_blog_posts.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return BlogPosts.objects.filter(is_published=True)


class BlogPostsByCategory(ListView):
    model = BlogPosts
    template_name = 'blogeek/home_blog_posts.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return BlogPosts.objects.filter(category_id=self.kwargs['category_id'],
                                        is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context


class ViewBlogPosts(DetailView):
    model = BlogPosts
    template_name = 'blogeek/view_blogposts.html'
    context_object_name = 'blogposts_item'


class CreateBlogPosts(CreateView):
    form_class = PostsForm
    template_name = 'blogeek/add_posts.html'

