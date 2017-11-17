from __future__ import unicode_literals

from django.db import models

from .choices import DIFFICULTY_CHOICES

class PostManager(models.Manager):
    def active(self, *args, **kwargs):
        return super(PostManager, self).filter(draft=False)

# Create your models here.
class Topic(models.Model):
    title = models.CharField(max_length=50)
    
    def __str__(self):
        return str(self.title)
    def __unicode__(self):
        return str(self.title)

class Post(models.Model):
    topic   = models.ForeignKey(Topic, on_delete=models.CASCADE)      
    title   = models.CharField(max_length=150)
    content = models.TextField()
    draft   = models.BooleanField(default=False)
    difficulty = models.CharField(choices=DIFFICULTY_CHOICES, default='Easy', max_length=20)        
    timestamp = models.DateField(auto_now=False, auto_now_add=True)
    
    # Manager
    objects = PostManager()
    
    def __str__(self):
        return str(self.title)
    def __unicode__(self):
        return str(self.title)
    def is_draft(self):
        return self.draft

    @property
    def topic_name(self):
        return str(self.topic.title)
