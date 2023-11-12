from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import RegisterForm, SharePictureForm
from django.contrib.auth import login, logout, authenticate
from .models import Sharedpicture

# Create your views here.

def index(request):
    return render(request, "mysite/index.html")

def storage(request):
    if request.user.is_authenticated:
        shared_pictures=Sharedpicture.objects.filter(receiver=request.user)
    return render(request, "mysite/storage.html", {"shared_pictures": shared_pictures })

# def send(request):
#     return render(request, "mysite/send.html")

def sign_up(request):
    if request.method=='POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request, user)
            return redirect('/home')
    else:
        form=RegisterForm()
    return render(request, 'registration/sign-up.html',{"form":form})

def share_picture(request):
    if request.method == 'POST':
        form = SharePictureForm(request.POST, request.FILES)
        if form.is_valid():
            shared_picture = form.save(commit=False)  # Create the instance but don't save it yet
            shared_picture.sender = request.user  # Set the sender to the currently logged-in user
            shared_picture.save() 
            return redirect('/home')
    else:
        form = SharePictureForm()
    
    return render(request, 'mysite/send.html', {'form': form})