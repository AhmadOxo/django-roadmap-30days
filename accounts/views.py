from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import ProfileForm

def profile_view(request, username):
    user = get_object_or_404(User, username=username)
    posts = user.post_set.order_by('-created_at')[:5]
    return render(request, 'accounts/profile.html', {
        'profile_user': user,
        'posts': posts,
    })


@login_required
def profile_edit(request, username):
    if request.user.username != username:
        return redirect('user:profile', username=username)
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('user:profile', username=username)
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'accounts/profile_edit.html', {'form': form})