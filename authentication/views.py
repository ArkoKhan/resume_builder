from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import login, logout
# from resume_builder.views import appHome

# Create your views here.

def home (request):
    if request.user.is_authenticated:
        return redirect('app_home')
    return render(request, 'index.html')

def log_in(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                username = request.POST.get('username')
                password = request.POST.get('password')
                
                if User.objects.filter(username = username).exists():
                    user = auth.authenticate(username=username, password=password)
                    
                    if user:
                        login(request, user)
                        return redirect('home')
                    else:
                        messages.error(request, 'Wrong password')
                    
                elif User.objects.filter(email = username).exists():
                    name = User.objects.get(email= username).username
                    user = auth.authenticate(username = name, password=password)
                    if user:
                        login(request, user)
                        return redirect('home')
                    else:
                        messages.error(request, 'Wrong password')
                    
                else:
                    messages.error(request, 'User does not exist')
                

        else:
            form = LoginForm()
            
        context={
            'form': form,
            'title': 'Login',
        }
        
        return render(request, 'Auth/auth_form.html', context)
    
    
    
def sign_up(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            form = SignupForm(request.POST)
            if form.is_valid():
                username = request.POST.get('username')
                email = request.POST.get('email')
                email_confirm = request.POST.get('email_confirm')
                password = request.POST.get('password')
                password_confirm = request.POST.get('password_confirm')
                
                if email == email_confirm:
                    
                    if password == password_confirm:
                        if User.objects.filter(username=username).exists():
                            messages.error(request, 'Username already exists')
                        elif User.objects.filter(email=email).exists():
                            messages.error(request, 'Email already exists')
                        else:
                            user = User.objects.create_user(username=username, email=email, password=password)
                            user.save()
                            messages.success(request, 'Account created successfully')
                            return redirect('login')
                    
                    else:
                        messages.error(request, 'Passwords do not match')
                    
                else:
                    messages.error(request, 'Emails do not match')
                    
                
        else:
            form = SignupForm()
        
        context = {
            'form': form,
            'title': 'Sign Up',
        }
        
        return render(request, 'Auth/auth_form.html', context)
    
def log_out(request):
    logout(request)
    return redirect('home')