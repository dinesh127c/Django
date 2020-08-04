from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth


# Create your views here.


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        firstname = request.POST['first_name']
        lastname = request.POST['Last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        list=[request.POST['first_name']]
        print(list[0])
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username Taken')
                return redirect('register')
            elif User.objects.filter(email=email):
                messages.info(request, 'email already taken')
                return redirect('register')
            else:
                user = User.objects.create_user(first_name=firstname, last_name=lastname, username=username,
                                                email=email, password=password1)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'password not matching')
            return redirect('register')
        return redirect('/')
    else:
        return render(request, 'register.html')


def logout(request):
    auth.logout(request)
    return redirect("/")
