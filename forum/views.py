from django.http import HttpResponse
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
from django.db.models import F
from user.models import LikedTopic


# Points
# def add_points(request):
    

# Home
def home(request):
    context = {}

    if request.method == 'GET' and len(request.GET) != 0:
        context['topics'] = Topic.objects.filter(title__icontains=request.GET['keyword'])
    elif request.POST.get('topicBtn'):
        user = request.user
        topic = Topic.objects.get(id=request.POST.get('topicBtn'))
        if(not user.likedtopic_set.filter(topic=topic).exists()):
            likedObj = LikedTopic(liker=user,topic=topic)
            likedObj.save()
            topic.points = F('points') + 1
            topic.save(update_fields=["points"])
        elif(user.likedtopic_set.filter(topic=topic).exists()):
            user.likedtopic_set.get(topic=topic).delete()
            topic.points = F('points') - 1
            topic.save(update_fields=["points"])
        else:
            pass
        context['topics'] = Topic.objects.all()
    else:
        context['topics'] = Topic.objects.all()
    return render(request, 'forum/home.html', context)

# class TopicListView(ListView):
#     model = Topic
#     template_name = 'forum/home.html'
#     ordering = ['-date_posted']

#     def get_context_data(self, **kwargs):
#         # Call the base implementation first to get a context
#         context = super().get_context_data(**kwargs)
#         # Add in a QuerySet
#         context['topics'] = Topic.objects.filter(title__icontains="2")
#         context['kw'] = self.kwargs.get('keyword')
#         # if self.kwargs.get('keyword'):
#         #     context['topics'] = Topic.objects.filter(title__icontains=self.kwargs.get('keyword'))
#         # else:
#         #     context['topics'] = Topic.objects.all()
#         return context

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


