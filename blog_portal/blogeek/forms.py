import re

from django import forms
from django.core.exceptions import ValidationError

from .models import Category
from .models import BlogPosts


class PostsForm(forms.ModelForm):
    class Meta:
        model = BlogPosts
        fields = ['title', 'description', 'content', 'is_published', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 15}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('The name must not start with a number')
        return title
