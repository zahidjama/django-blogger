from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm

class signin_form(UserCreationForm):
    class Meta:
        model=models.CustomUser
        fields=[ 'name', 'phone', 'email', ]

class post_blog(forms.ModelForm):
#    content= forms.CharField(label='Description', widget=forms.Textarea(attrs={'class': 'ckeditor'}))
    class Meta:
        model=models.blogs
        fields=['title', 'image', 'content', ]