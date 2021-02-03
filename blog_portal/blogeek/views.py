from django.shortcuts import render
from django.http import HttpResponse
from .models import BlogPosts


def index(request):
    posts = BlogPosts.objects.order_by('-created_at')
    title = 'Список статей'
    return render(request, 'blogeek/index.html', {'posts': posts, 'title': title})
