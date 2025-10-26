from django.db.models.query import QuerySet
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.views.generic import ListView
from django.contrib import messages
from typing import Any
from .models import *
from .forms import *

""" FBV - Function Based View 
def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog/post_list.html', {'posts': posts})
    
def posts_by_category(request, category_slug):
    category = get_object_or_404(Category, slug = category_slug)
    posts = Post.objects.filter(categories = category).order_by('-created_at')
    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/posts_by_category.html', 
                  {
                      'category': category,
                      'posts': page_obj,
                      'page_obj': page_obj,
                  })
"""

@login_required
def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            messages.success(request, "Comment added successfully!")
            return redirect('post_detail', slug=post.slug)
    else:
        form = CommentForm()
    
    return render(request, "blog/post_detail.html", 
                  {"post": post,
                   'comments': comments,
                   'form': form
                   })

@login_required
def post_create(request):
    if request.method == 'POST':
        form = Postform(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            form.save_m2m()
            return redirect('post_detail', slug=post.slug)
    else:
        form = Postform()
    return render(request, 'blog/post_form.html', {'form':form})

@login_required
def post_update(request, slug):
    post = get_object_or_404(Post, slug=slug, author=request.user)
    if request.method == 'POST':
        form = Postform(request.POST,  instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = Postform(instance=post)
    return render(request, 'blog/post_form.html', {'form': form})

@login_required
def post_delete(request, slug):
    post = get_object_or_404(Post, slug=slug, author=request.user)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    return render(request, 'blog/post_confirm_delete.html', {'post': post})

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    ordering = ['-created_at']
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Category'] = Category.objects.all()
        return context
    
class PostsByCategoryView(ListView):
    model = Post
    template_name = 'blog/posts_by_category.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        category = get_object_or_404(Category, slug=self.kwargs['category_slug'])
        qs = Post.objects.filter(categories=category).order_by('-created_at')
        print(f"Category: {category.name} (slug: {self.kwargs['category_slug']})")
        print(f"Filtered posts: {qs.count()}")
        print(f"Post titles: {[post.title for post in qs]}")
        print(f"Page size: {self.paginate_by}")
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = get_object_or_404(Category, slug=self.kwargs['category_slug'])
        context['categories'] = Category.objects.all()  # For sidebar
        return context

class SearchView(ListView):
    model = Post
    template_name = 'blog/search_results.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        query = self.request.GET.get('q')
        page = self.request.GET.get('page', '1')
        print(f"Query parameter: {query}, Page: {page}")
        if query:
            qs = Post.objects.filter(
                Q(title__icontains=query) | Q(content__icontains=query)
            ).order_by('-created_at')
            print(f"Search query: {query}, Results: {qs.count()}")
            print(f"Post titles: {[post.title for post in qs]}")
            print(f"Rendering template: {self.template_name}")
            return qs
        print("No query provided, returning empty queryset")
        return Post.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q', '')
        print(f"Context query: {query}")
        context['query'] = query
        context['categories'] = Category.objects.all()
        return context

# class SearchView(ListView):
#     model = Post
#     template_name = 'blog/search_results.html'
#     context_object_name = 'posts'
#     paginate_by = 5

#     def get_queryset(self):
#         query = self.request.GET.get('q')
#         if query:
#             qs = Post.objects.filter(
#                 Q(title__icontains=query) | Q(content__icontains=query)
#             ).order_by('-created_at')
#             return qs
#         return Post.objects.none()
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['query'] = self.request.GET.get('q', '')
#         context['categories'] = Category.objects.all()
#         print(f"Rendering template: {self.template_name}")
#         return context