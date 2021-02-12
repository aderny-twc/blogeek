from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView

from .forms import PostsForm
from .models import BlogPosts, Category


class HomeBlogPosts(ListView):
    model = BlogPosts
    template_name = 'blogeek/home_blog_posts.html'

    def get_queryset(self):
        return BlogPosts.objects.filter(is_published=True)


def get_category(request, category_id):
    posts = BlogPosts.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    context = {
        'posts': posts,
        'category': category,
    }
    return render(request, 'blogeek/category.html', context)


def view_blogposts(request, blogposts_id):
    blogposts_item = get_object_or_404(BlogPosts, pk=blogposts_id)
    # blogposts_item = BlogPosts.objects.get(pk=blogposts_id)
    return render(request, 'blogeek/view_blogposts.html', {"blogposts_item": blogposts_item})


def add_posts(request):
    if request.method == 'POST':
        form = PostsForm(request.POST)
        if form.is_valid():
            form.cleaned_data['user_id'] = request.user.id
            post = BlogPosts.objects.create(**form.cleaned_data)
            return redirect(post)
    else:
        form = PostsForm()

    title = 'Create posts'
    context = {
        'title': title,
        'form': form,
    }
    return render(request, 'blogeek/add_posts.html', context)
