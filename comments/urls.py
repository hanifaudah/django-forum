from django.urls import path, include
from .views import (
    CommentCreateView,
    CommentUpdateView,
    CommentDeleteView,
)

urlpatterns = [
    path('new/<str:type>/<int:pk_parent>/', CommentCreateView.as_view(), name='comment-create'),
    path('update/<int:pk3>/', CommentUpdateView.as_view(), name='comment-update'),
    path('delete/<int:pk3>/', CommentDeleteView.as_view(), name='comment-delete'),
]