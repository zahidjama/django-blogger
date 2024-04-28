from django.shortcuts import render, redirect
from . import forms
from . import models
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url="/login")
def dashboard(request):
    if request.user.is_authenticated:
        user_login=True
    else:
        user_login=False
    return render(request, "dashboard.html", {'user_login':user_login})

def myuploads(request):
    obj=models.blogs.objects.filter(uploader=request.user)
    if request.user.is_authenticated:
        user_login=True
    else:
        user_login=False
    return render(request, "index.html", {'data':obj, 'user_login':user_login})


def readpost(request):
    Id=request.GET.get("id")
    obj=models.blogs.objects.filter(id=Id)
    if request.user.is_authenticated:
        user_login=True
    else:
        user_login=False
    return render(request, "readpost.html", {"data":obj, 'user_login': user_login})

def index(request):
    obj=models.blogs.objects.all().order_by("-id")
    if request.user.is_authenticated:
        user_login=True
    else:
        user_login=False
    return render(request, "index.html", {'data':obj, 'user_login':user_login})

@login_required(login_url="login")
def create_blog(request):
    form=forms.post_blog(request.POST, request.FILES)
    if form.is_valid():
        print(request.user.name)
        obj=models.blogs()
        title=request.POST.get("title")
        content=request.POST.get("content")
        img=request.FILES.get("image")

        obj.title=title
        obj.content=content
        obj.image=img
        obj.uploader=request.user

        obj.save()
    if request.user.is_authenticated:
        user_login=True
    else:
        user_login=False
    return render(request, "create_blog.html", {'form':form, 'user_login':user_login})

@login_required(login_url="/login")
def logout_user(request):
    logout(request)
    return redirect("/login")

def login_user(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    form=AuthenticationForm()
    if request.method=='POST':
        uemail=request.POST.get("username")
        upass=request.POST.get("password")
        user=authenticate(request, email=uemail, password=upass)
        if user is not None:
            login(request, user)
            return redirect("dashboard")

    if request.user.is_authenticated:
        user_login=True
    else:
        user_login=False
    return render(request, "login.html", {'form':form, 'user_login': user_login})

def signin(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    form=forms.signin_form(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("Login")
    if request.user.is_authenticated:
        user_login=True
    else:
        user_login=False
    return render(request, "signin.html", {'form': form, 'user_login':user_login})