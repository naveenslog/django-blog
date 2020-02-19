from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    craeted_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
  
    def __str__(self):
        return self.name