from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

# Register View
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('forum-home')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form':form})

@login_required
def profile(request):
    return render(request, 'user/profile.html')
