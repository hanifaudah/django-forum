from django.contrib import admin
from .models import Profile, LikedTopic, LikedPost

admin.site.register(Profile)
admin.site.register(LikedTopic)
admin.site.register(LikedPost)


