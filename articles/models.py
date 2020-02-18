# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now=False, auto_now_add=True)
    thumb = models.ImageField(blank=True,default='default.png')
      
    def __str__(self):
        return self.title
    
    def snippet(self):
        return self.body