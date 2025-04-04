from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .models import projeto

# Create your views here.

def PortalExtensaoView(request):
    return render(request, 'admin-cards.html',{'current_page':'admin-cards'})
def AdminPageView(request):
    return render(request, 'admin-cards.html',{'current_page':'admin-cards'})
def AdminTable(request):
    return render(request, 'admin-table.html',{'current_page':'admin-table'})
def Create(request):
    return render(request, 'create.html',{'current_page':'create'})




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
    projeto_detail = get_object_or_404(projeto, id=projeto_id)
    return render(request, 'project.html', {'projeto': projeto_detail})

def ProjectCreate(request):
    if request.method == "POST'":
        nome = request.post['project-name']
        coordenador = request.post['professor-name']
        curso = request.post['degree']

        projeto = projeto(nome=nome,coordenador=coordenador,curso=curso)
        projeto.save()
        return redirect('base')
    return render('create.html')