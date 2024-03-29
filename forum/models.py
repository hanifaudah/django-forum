from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Topic(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)

    class Meta:
        ordering = ['-points']

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-list', kwargs={
            'pk1':self.pk
        })