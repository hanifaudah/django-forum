from django.db import models
from django.contrib.auth.models import User
from forum.models import Topic
from django.utils import timezone
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail',kwargs={
            'pk2':self.pk,
            'pk1':self.topic.id,
        })