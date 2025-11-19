from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.text import slugify
from django.db.models import Q
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

from .models import Post,Comment
from .forms import PostForm,CommentForm

# Create your views here.
def home(request):
    feedback = None
    featured_post = Post.objects.get(featured=True)
    posts = Post.objects.filter(featured=False)
    keyword = request.GET.get('search')
    if keyword:
        posts = Post.objects.filter(Q(title__icontains=keyword) | Q(content__icontains=keyword) | Q(category__title__icontains=keyword))
        if posts.exists():
            featured_post = None
        else:
            feedback = 'No post found with that keyword'
            featured_post = None
    paginate = Paginator(posts, 2)
    page = request.GET.get('page')
    try:
        posts = paginate.page(page)
    except PageNotAnInteger:
        posts = paginate.page(1)
    except EmptyPage:
        posts = paginate.page(paginate.num_pages)
    context = {'featured_post':featured_post,'posts':posts,'feedback':feedback,'paginate':paginate}
    return render(request,'posts/home.html',context)


def detail(request,slug):
    post = Post.objects.get(slug=slug)
    comments = Comment.objects.filter(post=post)
    form = CommentForm()
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.post = post
                comment.user = request.user
                comment.save()
                return redirect('posts:detail',slug=post.slug)
        else:
            return redirect('users:login')
    context = {'post':post,'form':form,'comments':comments}
    return render(request,'posts/detail.html',context)


@login_required(login_url='users:login')
def add_post(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.slug = slugify(request.POST.get('title'))
            post.user = request.user
            post.save()
            messages.success(request,'Post created successfully')
            return redirect('users:profile')
    context = {'form':form}
    return render(request,'posts/add.html',context)


@login_required(login_url='users:login')
def update_post(request,slug):
    update = True
    post = Post.objects.get(slug=slug)
    form = PostForm(instance=post)
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            update_form = form.save(commit=False)
            update_form.slug = slugify(request.POST.get('title'))
            update_form.save()
            messages.success(request,'Post updated successfully!')
            return redirect('users:profile')
    context = {'update':update,'form':form}
    return render(request,'posts/add.html',context)


@login_required(login_url='users:login')
def delete_post(request,slug):
    delete = True
    post = Post.objects.get(slug=slug)
    posts = Post.objects.filter(user=request.user)
    if request.method == 'POST':
        post.delete()
        messages.error(request,'Post deleted successfully')
        return redirect('users:profile')
    context = {'delete':delete,'post':post,'posts':posts}
    return render(request,'users/profile.html',context)

