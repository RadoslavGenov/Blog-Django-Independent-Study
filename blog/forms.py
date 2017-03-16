from .models import Comment, Post
from taggit.forms import *


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)


class PostForm(forms.ModelForm):
    tags = TagField()

    class Meta:
        model = Post
        fields = ('title', 'author', 'body', 'publish',)