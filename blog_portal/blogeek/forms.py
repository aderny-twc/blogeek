from django import forms
from .models import Category


class PostsForm(forms.Form):
    title = forms.CharField(max_length=150, label='Title', widget=forms.TextInput(attrs={"class": "form-control"}))
    description = forms.CharField(label='Description', widget=forms.Textarea(attrs={"class": "form-control",
                                                                                    'rows': 5, }))
    content = forms.CharField(label='Content', widget=forms.Textarea(attrs={"class": "form-control",
                                                                            'rows': 15,}))
    is_published = forms.BooleanField(label='Post', initial=True)
    category = forms.ModelChoiceField(queryset=Category.objects.all(),
                                      empty_label='Choose',
                                      label='Category',
                                      widget=forms.Select(attrs={"class": "form-control"}))