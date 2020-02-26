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
        type = self.kwargs.get('type')
        if type == 'Post':
            form.instance.parent = None
        elif type == 'Comment':
            form.instance.parent = Comment.objects.get(pk=self.kwargs.get('pk_parent'))
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)

            #This works
            post = Post.objects.get(pk=self.kwargs.get('pk2'))
            context['pk1'] = post.topic.id
            context['pk2'] = self.kwargs.get('pk2')
            return context

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
    
    def get_context_data(self, **kwargs):
            # Call the base implementation first to get a context
            context = super().get_context_data(**kwargs)
            # Add in a QuerySet of all the books
            comment = self.get_object()
            context['pk1'] = comment.id
            context['pk2'] = self.kwargs.get('pk2')
            return context

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

