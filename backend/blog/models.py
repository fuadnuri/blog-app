from django.db import models
from django.utils import timezone 
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now)
    def __str__(self):
        return self.title
# class PostLike()



class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name="comments",on_delete=models.CASCADE)
    comment = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    
    def __str__(self):
        return self.comment 


class LikeComment(models.Model):
    comment = models.OneToOneField(Comment, related_name='likes', on_delete=models.CASCADE)
    users = models.ManyToManyField(User, related_name='requirement_comment_like')
    def __str__(self):
        return str(self.comment.comment)
