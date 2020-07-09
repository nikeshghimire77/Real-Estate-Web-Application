from django.shortcuts import redirect, render
from django.contrib import auth, messages
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        #Get forms values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if  password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
                return('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already exists')
                    return ('register')
                else:
                    user = User.objects.create_user(
                        username=username, first_name=first_name, last_name=last_name,password=password, email=email
                    )
                    user.save()
                    messages.success(request, ' You are now registered. Please enter your credentials')
                    return redirect('login')
        else:
            messages.error(request, 'Password do not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')
    
    return render(request, 'accounts/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Username or password do not match')
            return redirect('login')

    else:
        return render(request, 'accounts/login.html')
    return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request,'You are now logged out')
        return redirect('index')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')