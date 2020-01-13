from django.urls import path, include
from .views import (
    TopicDetailView,
    TopicCreateView,
    TopicUpdateView,
    TopicDeleteView,
)
from . import views

urlpatterns = [
    path('', views.home, name='forum-home'),
    # path('', TopicListView.as_view(), name='forum-home'),
    path('topicdetail/<int:pk1>/', include('posts.urls')),
    path('topicdetail/<int:pk1>/update/', TopicUpdateView.as_view(), name='topic-update'),
    path('topiccreate/', TopicCreateView.as_view(), name='topic-create'),
    path('topicdelete/<int:pk1>/', TopicDeleteView.as_view(), name='topic-delete'),
]