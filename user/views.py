from django.contrib import messages, auth
from django.shortcuts import redirect, render

def login(request):
    return render(request, 'user/login.html')

def register(request):
    return render(request, 'user/register.html')

def logout(request):
    messages.success(request, 'Logout successful!')
    auth.logout(request)
    return redirect('login')