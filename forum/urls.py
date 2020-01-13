from django.urls import path, include
from .views import (
    TopicListView,
    TopicDetailView,
    TopicCreateView,
    TopicUpdateView,
    TopicDeleteView,
)

urlpatterns = [
    path('', TopicListView.as_view(), name='forum-home'),
    path('topicdetail/<int:pk1>/', include('posts.urls')),
    path('topicdetail/<int:pk1>/update/', TopicUpdateView.as_view(), name='topic-update'),
    path('topiccreate/', TopicCreateView.as_view(), name='topic-create'),
    path('topicdelete/<int:pk1>/', TopicDeleteView.as_view(), name='topic-delete'),
]