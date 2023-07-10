from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField("포스트 제목", max_length=255)
    content = models.TextField("포스트 내용")
    user = models.TextField("사용자 이름")
    passwords = models.TextField("비밀번호", default="")
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField("댓글 내용")
    user = models.TextField("사용자 이름")
    passwords = models.TextField("비밀번호", default="")
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.post.title}의 댓글 (작성자: {self.user}) (내용: {self.content})"