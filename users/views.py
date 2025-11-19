from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm,UpdateProfileForm
from posts.models import Post

# Create your views here.

def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Account created successfully')
            return redirect('posts:home')
    
    context = {'form':form}
    return render(request,'users/register.html',context)


def signin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request,email=email,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'You are now logged in!')
            goto = request.GET.get('next')
            if goto:
                return redirect(goto)
            return redirect('posts:home')
        else:
            messages.error(request,'Invalid username or password')
            return redirect('users:login')
        
    return render(request,'users/login.html')


@login_required(login_url='users:login')
def signout(request):
    logout(request)
    messages.error(request,'You are now logged out')
    return redirect('users:login')


@login_required(login_url='users:login')
def profile(request):
    user = request.user
    posts = Post.objects.filter(user=user)
    context = {'user':user,'posts':posts}
    return render(request,'users/profile.html',context)


@login_required(login_url='users:login')
def update_profile(request):
    if request.user.is_authenticated:
        user = request.user
        form  = UpdateProfileForm(instance=user)
        if request.method == 'POST':
            form = UpdateProfileForm(request.POST,request.FILES,instance=user)
            if form.is_valid():
                form.save()
                messages.success(request,'Profile Updated Successfully!')
                return redirect('users:profile')

        context = {'form':form}
        return render(request,'users/update_profile.html',context)
    return redirect('users:login')