from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .models import projeto

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

def ProjectView(request, projeto_id):
    if request.method == "GET":
        try:
            projeto_detail = project.objects.filter(id=projeto_id)
        except ObjectDoesNotExist:
            messages.error(request, 'Projeto não encontrado')
            redirect('project')
    return render(request, 'project.html', {'projeto': projeto_detail})