from django.db import models
from datetime import datetime
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    photo = models.URLField(blank=True)
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now=True)
# 記得加 models.資料型態
    def __str__(self):
        return self.title
