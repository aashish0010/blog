from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    image = models.ImageField(upload_to='images')
    title = models.CharField(max_length=222,null=True,blank=True,default=None)
    content = HTMLField(default=None)
    date_added = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts',default=True)

    def __str__(self):
        return self.title


    class Meta:
        ordering = ['-date_added']