from django.db import models
from posts.models import Post
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey

class Comment(MPTTModel):
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children', default=0)

    def __str__(self):
        return self.content
    
    def get_absolute_url(self):
        return reverse('post-detail',kwargs={
            'pk2':self.post.pk,
            'pk1':self.post.topic.id,
        })
    
    class MPTTMeta:
        order_insertion_by = ['date_posted']
        
