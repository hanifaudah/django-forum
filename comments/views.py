from django.shortcuts import render
from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse
from .models import Comment
from posts.models import Post

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['content']

    def form_valid(self, form):
        form.instance.author = self.request.user 
        form.instance.post = Post.objects.get(pk=self.kwargs.get('pk2'))
        return super().form_valid(form)

class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin ,UpdateView):
    model = Comment
    fields = ['content']
    pk_url_kwarg = 'pk3'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = Post.objects.get(pk=self.kwargs.get('pk2'))
        return super().form_valid(form)
     
    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    pk_url_kwarg = 'pk3'

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author
    
    def get_success_url(self):
        comment = self.get_object()
        return reverse('post-detail', kwargs={
            'pk1':comment.post.topic.id,
            'pk2':self.kwargs.get('pk2'),
        })

