from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
# Create your views here.

def PortalExtensaoView(request):
    return render(request, 'admin-cards.html')

def AdminPageView(request):
    return render(request, 'admin-cards.html')

def Create(request):
    return render(request, 'create.html')

def LoginView(request):
    if request.method == "POST":
        email = request.post['email']
        password = request.post['password']
        user = authenticate(request=request, email=email, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('admin')
        else:
            messages.error(request, 'E-mail ou Senha incorreto')            
            redirect('login')
    return render(request, 'login.html')

