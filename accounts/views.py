from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect
from django.contrib.auth.models import User
from .forms import UserForm

# Create your views here.

def register(request):
        if request.method == "POST":
            form = UserForm(request.POST)

            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                return redirect('/')
                
        else:
            form = UserForm()
        
        return render(request,'register.html',{'form' : form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data = request.POST)

        if form.is_valid():
            login(request, form.get_user())
            return redirect('/')
    else:
        form = AuthenticationForm()

    return render(request,'login.html',{'form' : form})

def logout_view(request):
    logout(request)
    return redirect('/')

def profile(request,username):
    user = User.objects.get(username=username)
    return render(request, 'profile.html', {'user' : user})