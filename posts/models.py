from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title
    

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,blank=True,null=True,related_name='posts')
    title = models.CharField(max_length=100,unique=True)
    slug = models.SlugField()
    content = models.TextField()
    thumbnail = models.ImageField(upload_to='postimg')
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    featured = models.BooleanField(default=False)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,blank=True,null=True,related_name='posts')

    def __str__(self):
        return self.title
    


class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='comments')
    content = models.TextField()
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content