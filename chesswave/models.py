from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Game(models.Model):
    author = models.ForeignKey('auth.User', blank = True, null = True)
    white = models.CharField(max_length=50, blank=True, null=True)
    black = models.CharField(max_length=50, blank=True, null=True)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
              
    def publish(self):
        self.published_date = timezone.now() 
        self.save()
                   
    def __str__(self):
        return self.white       


class Move(models.Model):
    game = models.ForeignKey(Game)
    move = models.CharField(max_length=10)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
            
    def publish(self):
        self.published_date = timezone.now() 
        self.save()
            
    def __str__(self):
        return self.move        
        
        
class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title  
