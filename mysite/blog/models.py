from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date 

# Create your models here.
STATUS = (
    (0,'Draft'),
    (1,'Publish'),
)
    
class Posts(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    photo = models.ImageField(blank = True) 
    content = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=30, default = 'not categorized')
    likes = models.ManyToManyField(User, related_name='blog_post') 

    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        #return reverse('post', args = str(self.pk))
        return reverse('home')
    
    def total_likes(self):
        return self.likes.count()

class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('home')



