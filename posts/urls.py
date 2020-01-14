from django.urls import path, include
from .views import (
    # PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)
from . import views

urlpatterns = [
    path('', views.home, name='post-list'),
    # path('', PostListView.as_view(), name='post-list'),
    # path('comments/', include('comments.urls')),
    path('post/<int:pk2>/detail/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk2>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk2>/delete/', PostDeleteView.as_view(), name='post-delete'),
]