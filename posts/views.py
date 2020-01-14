from django.shortcuts import render
from posts.models import Post
from forum.models import Topic
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse


def home(request, pk1):
    context = {
        'topic':Topic.objects.get(pk=pk1),
    }
    ordering = ['-date_posted']
    if request.method == 'GET' and len(request.GET) != 0:
        context['posts'] = Post.objects.filter(topic=pk1).filter(title__icontains=request.GET['keyword'])
    else:
        context['posts'] = Post.objects.filter(topic=pk1)
    return render(request, 'posts/post_list.html', context)

# class PostListView(ListView):
#     model = Post
    
#     def get_context_data(self, **kwargs):
#         # Call the base implementation first to get a context
#         context = super().get_context_data(**kwargs)
#         # Add in a QuerySet of all the books
#         context['posts'] = Post.objects.filter(topic=self.kwargs.get('pk1'))
#         context['topic'] = Topic.objects.get(pk=self.kwargs.get('pk1'))
#         return context

class PostDetailView(DetailView):
    model = Post
    pk_url_kwarg = 'pk2'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title','content']
    pk_url_kwarg = 'pk2'

    def form_valid(self, form):
        form.instance.author = self.request.user 
        form.instance.topic = Topic.objects.get(pk=self.kwargs.get('pk1'))
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['pk1'] = self.kwargs.get('pk1')
        return context

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title','content']
    pk_url_kwarg = 'pk2'

    def form_valid(self, form):
        form.instance.author = self.request.user 
        return super().form_valid(form)
     
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['pk1'] = self.kwargs.get('pk1')
        return context

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    pk_url_kwarg = 'pk2'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    
    def get_success_url(self):
        return reverse('post-list', kwargs={'pk1':self.kwargs.get('pk1')})
