from django.contrib import messages, auth
from django.shortcuts import redirect, render
from user.forms import LoginForms, registerForms
from django.contrib.auth.models import User

def login(request):
    form = LoginForms()

    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():
            name = form['username'].value()
            password = form['password'].value()

        user = auth.authenticate(
            request,
            username = name,
            password = password
        )

        if user is not None:
            auth.login(request, user)
            messages.success(request, f'{name} logged in successfully')
            return redirect('index')
        else:
            messages.error(request, f'{name} error logging in')
            return redirect('login')
        
    
    return render(request, 'user/login.html', {'form': form})

def register(request):
    form = registerForms()

    if request.method == 'POST':
        form = registerForms(request.POST)

        if form.is_valid():
            if form['password1'].value() != form['password2'].value():
                messages.error(request, 'Password are not the same')
                return redirect('register')
            
            name = form['register_username'].value()
            email = form['email'].value()
            password = form['password1'].value()

            if User.objects.filter(username=name).exists():
                messages.error(request, 'This username already exists')
                return redirect('register')
            
            user = User.objects.create_user(
                username = name,
                email = email,
                password = password
            )
            user.save()
            messages.success(request, f'{name} registration completed successfully')
            return redirect('login')

    return render(request, 'user/register.html', {'form': form})

def logout(request):
    messages.success(request, 'Logout successful!')
    auth.logout(request)
    return redirect('login')