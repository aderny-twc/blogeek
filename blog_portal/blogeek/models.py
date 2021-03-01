from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


class BlogPosts(models.Model):
    """
    Blog article class.
    """
    title = models.CharField(max_length=150, verbose_name='Title')
    description = models.CharField(max_length=600, verbose_name='Description')
    content = models.TextField(blank=True, verbose_name='content')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated at')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Photo', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Is published')
    views = models.IntegerField(default=0)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Category')
    user = models.ForeignKey(User, verbose_name="Автор", on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-created_at']

    def get_absolute_url(self):
        return reverse('view_blogposts', kwargs={"pk": self.pk})

    def __str__(self):
        return self.title


class Category(models.Model):
    """
    Article category class.
    """
    title = models.CharField(max_length=150, db_index=True, verbose_name='Категория')
    description = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']

    def get_absolute_url(self):
        return reverse('category', kwargs={"category_id": self.pk})

    def __str__(self):
        return self.title
