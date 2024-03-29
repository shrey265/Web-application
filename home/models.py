import imp
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
from .helpers import *

class profile(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        is_verified = models.BooleanField(default=False)
        token = models.CharField(max_length=100)


        
class pictureModel(models.Model):
        title = models.CharField(max_length=1000)
        story = models.TextField()
        slug = models.SlugField(max_length=1000,null=True,blank=True)
        user = models.ForeignKey(User,blank=True,null=True, on_delete=models.CASCADE)
        image = models.ImageField(upload_to='picture_store')
        created_at = models.DateTimeField(auto_now_add=True)
        upload_to = models.DateTimeField(auto_now=True)

        def __str__(self):
            return self.title

        def save(self,*args,**kwargs):
                self.slug = generate_slug(self.title)
                super(pictureModel, self).save(*args, **kwargs)
        

