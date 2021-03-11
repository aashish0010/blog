from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Post


# Create your views here.

def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username taken')
                return redirect('signup')

            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email already taken')
                return redirect('signup')

            else:
                user = User.objects.create_user(username=username, password=password1, email=email)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'password does not match')
            return redirect('signup')

    return render(request, 'signup.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')

        else:
            messages.info(request, 'invalid username or password')
            return redirect('login')
    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('login')


def profile(request):
    return render(request, 'profile.html')


def post(request):
    data = Post.objects.all()
    if request.method == 'POST':
        image= request.POST['image']
        title = request.POST['title']
        content = request.POST['content']
        if not title:
            messages.info(request, 'please provide title')
            return redirect('post')
        elif not content:
            messages.info(request, 'please provide content')
            return redirect('post')

        elif not image:
            messages.info(request,'please add a image')
            return redirect('post')

        else:
            post = Post(title=title, content=content ,image=image)
            post.save()

    return render(request, 'post.html', {'data': data})