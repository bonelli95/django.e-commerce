from django.contrib import messages, auth
from django.shortcuts import redirect, render
from user.forms import LoginForms, registerForms

def login(request):
    form = LoginForms()
    return render(request, 'user/login.html', {'form': form})

def register(request):
    form = registerForms()
    return render(request, 'user/register.html', {'form': form})

def logout(request):
    messages.success(request, 'Logout successful!')
    auth.logout(request)
    return redirect('login')