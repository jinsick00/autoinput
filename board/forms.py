from django import forms
from board.models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'user', 'passwords']
        labels = {
            'title' : '제목',
            'content' : '본문',
            'user' : '작성자',
            'passwords' : '비밀번호',
        }