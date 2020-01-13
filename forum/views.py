from django.shortcuts import render
from .models import Topic
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# Home
def home(request):
    context = {
        'topics':Topic.objects.all(),
    }
    return render(request, 'forum/home.html', context)

class TopicListView(ListView):
    model = Topic
    template_name = 'forum/home.html'
    context_object_name = 'topics'
    ordering = ['-date_posted']

class TopicDetailView(DetailView):
    model = Topic
    pk_url_kwarg = 'pk1'

class TopicCreateView(LoginRequiredMixin, CreateView):
    model = Topic
    fields = ['title','content']
    pk_url_kwarg = 'pk1'

    def form_valid(self, form):
        form.instance.author = self.request.user 
        return super().form_valid(form)

class TopicUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Topic
    fields = ['title','content']
    pk_url_kwarg = 'pk1'

    def form_valid(self, form):
        form.instance.author = self.request.user 
        return super().form_valid(form)
     
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class TopicDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Topic
    success_url = '/'
    pk_url_kwarg = 'pk1'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


