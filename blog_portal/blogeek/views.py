from django.shortcuts import render
from .models import BlogPosts, Category


def index(request):
    posts = BlogPosts.objects.order_by('-created_at')
    categories = Category.objects.all()
    title = 'Список статей'
    context = {
        'posts': posts,
        'title': title,
        'categories': categories,
    }
    return render(request, 'blogeek/index.html', context)


def get_category(request, category_id):
    posts = BlogPosts.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    context = {
        'posts': posts,
        'categories': categories,
        'category': category,
    }
    return render(request, 'blogeek/category.html', context)
