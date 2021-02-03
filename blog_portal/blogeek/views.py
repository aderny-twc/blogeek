from django.shortcuts import render
from .models import BlogPosts, Category


def index(request):
    posts = BlogPosts.objects.order_by('-created_at')
    title = 'Список статей'
    context = {
        'posts': posts,
        'title': title,
    }
    return render(request, 'blogeek/index.html', context)


def get_category(request, category_id):
    posts = BlogPosts.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    context = {
        'posts': posts,
        'category': category,
    }
    return render(request, 'blogeek/category.html', context)
