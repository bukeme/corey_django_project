from blog.models import Post
from django import forms
from django.shortcuts import redirect

class CreateViewForm(forms.ModelForm):
    
    


    class Meta:
        model = Post
        fields = ['title', 'content']
    