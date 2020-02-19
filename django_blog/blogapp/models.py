from django.db import models
from common.models import Category
from django.contrib.auth.models import User

class Post(models.Model):
    title       = models.CharField(max_length=255)
    content     = models.TextField()
    is_featured = models.BooleanField(default=False)
    categories  = models.ManyToManyField(Category, null=True, blank=True)
    author      = models.ForeignKey(User,on_delete=models.CASCADE, default=1)
    craeted_at  = models.DateTimeField(auto_now=True)
    updated_at  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title