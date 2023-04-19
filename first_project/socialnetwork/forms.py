from django import forms
from socialnetwork.models import Comment,Post


class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields = ['body']

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields = ['title','body']