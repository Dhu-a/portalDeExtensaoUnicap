from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .models import projeto

# Create your views here.

def PortalExtensaoView(request):
    return render(request, 'admin-cards.html',{'current_page':'admin-cards'})
def AdminPageView(request):
    return render(request, 'admin-cards.html',{'current_page':'admin-cards'})
#def AdminTable(request):
#    return render(request, 'admin-table.html',{'current_page':'admin-table'})
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
    projeto_detail = get_object_or_404(projeto, id=projeto_id)
    return render(request, 'project.html', {'projeto': projeto_detail})

def ProjectCreate(request):
    if request.method == "POST":
        identificacao_unica = request.POST.get('identifier')
        titulo = request.POST.get('project-name')
        proposta = request.POST.get('proposal')
        curso = request.POST.get('degree')
        coordenador = request.POST.get('professor-name')
        ch_total = request.POST.get('total-hours')
        ch_semanal_docente = request.POST.get('weekly-hours-professor')
        ch_semanal_estudante = request.POST.get('weekly-hours-student')
        data_inicio = request.POST.get('start-date')
        data_termino = request.POST.get('end-date')
        instagram = request.POST.get('instagram')
        contato = request.POST.get('contact')
        formulario = request.POST.get('formulary')

        projetoNovo = projeto(identificacao_unica=identificacao_unica, titulo=titulo, proposta=proposta, 
                            curso=curso, coordenador=coordenador,ch_total=ch_total, 
                            ch_semanal_docente=ch_semanal_docente, 
                            ch_semanal_estudante=ch_semanal_estudante, data_inicio=data_inicio,
                            data_termino=data_termino, instagram=instagram, contato=contato, 
                            formulario=formulario)
        projetoNovo.save()
    return render(request, 'create.html')