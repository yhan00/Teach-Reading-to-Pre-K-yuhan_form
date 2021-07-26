from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            return redirect('dashboard')
        else:
            messages.info(request, 'invalid credentials')
            return redirect("users:register")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form':form})

def logout(request):
    auth.logout(request)
    return redirect('/')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth.login(request, user)
            return redirect('dashboard')
        else:
            messages.info(request, 'Error')
            return redirect("users:register")
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

