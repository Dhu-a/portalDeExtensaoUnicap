from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from .models import projeto, dias,areas
from django.http import HttpResponse, Http404
from django.template import loader

# Create your views here.

def PortalExtensaoView(request):
    projetos = projeto.objects.all()
    cursos=projeto.objects.values_list('curso', flat=True).distinct()
    areas_lista=areas.objects.values_list('area', flat=True).distinct();
    

#filtrar pela area selecionada
    area_filter=request.GET.get('area')
    if area_filter:
        projetos=projetos.filter(areas__area=area_filter).distinct()

#filtrar pelo turno selecionado
    turno_filter=request.GET.get('turno')
    if turno_filter:
        projetos=projetos.filter(dias__turno=turno_filter).distinct()

#filtrar pelo dia selecionado
    dia_filter=request.GET.get('dia')
    if dia_filter:
        projetos=projetos.filter(dias__dia=dia_filter).distinct()

#filtrar pelo local selecionado
    local_filter=request.GET.get('local')
    if local_filter:
        projetos=projetos.filter(dias__lugar=local_filter).distinct()

#filtrar pelo curso selecionado
    curso_filter=request.GET.get('curso')
    if curso_filter:
        projetos=projetos.filter(curso=curso_filter)

#filtrar por nome digitado
    search_name=request.GET.get('search_name')
    if search_name:
        projetos=projetos.filter(titulo__icontains=search_name)

#filtrar por vagas abertas
    vagas_filter=request.GET.get('vagas');
    if vagas_filter=="1":
        projetos=projetos.filter(aceitando=True);
    
    return render(request, 'admin-cards.html', {
        'current_page': 'public-cards',
        'portalExtensaoUnicap_app_projetos': projetos,
        'cursos': cursos,
        'areas_lista': areas_lista,
    })


def AdminPageView(request):
    projetos = projeto.objects.all()
    cursos = projeto.objects.values_list('curso', flat=True).distinct()
    

    curso_filter = request.GET.get('curso')
    if curso_filter:
        projetos = projetos.filter(curso=curso_filter)
    
    return render(request, 'admin-cards.html', {
        'current_page': 'public-cards',
        'portalExtensaoUnicap_app_projetos': projetos,
        'cursos': cursos,
    })
#def AdminTable(request):
#    return render(request, 'admin-table.html',{'current_page':'admin-table'})
def Create(request):
    return render(request, 'create.html')




def LoginView(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        username = User.objects.get(email=email)
        user = authenticate(request, username=username.username, password=password)

        if user is not None:
            login(request, user)
            return redirect('admin')
        else:
            messages.error(request, 'E-mail ou Senha incorreto')
            redirect('login')
    return render(request, 'login.html')

def ProjectView(request, projeto_id):
    # função de deletar:
    if request.method == 'GET' and request.GET.get('delete') != None:
        projeto.objects.filter(id=projeto_id).delete()
        return redirect('admin')
    #pág carregando:
    projeto_detail = get_object_or_404(projeto, id=projeto_id)
    return render(request, 'project.html', {'projeto': projeto_detail})

def ProjectCreate(request):
    if request.method == "POST":
        identificacao_unica = request.POST.get('identifier')
        titulo = request.POST.get('project-name')
        proposta = request.POST.get('proposal')
        area = request.POST.get('area')
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
        aceitando = request.POST.get('availability')
        if aceitando == "on":
            aceitando = True
        else:
            aceitando = False
        projetoNovo = projeto(identificacao_unica=identificacao_unica, titulo=titulo, proposta=proposta, 
                            curso=curso, coordenador=coordenador,ch_total=ch_total, 
                            ch_semanal_docente=ch_semanal_docente, 
                            ch_semanal_estudante=ch_semanal_estudante, data_inicio=data_inicio,
                            data_termino=data_termino, instagram=instagram, contato=contato, 
                            formulario=formulario, aceitando=aceitando)
        projetoNovo.save()

        #add na table de area mas ele soh ta aceitando 1 area, ajeitar isso dps
        areaNovo=areas(id_projeto=projetoNovo, area=area);
        areaNovo.save();

        dias_e_turnos = request.POST.getlist('schedule')
        locais1 = request.POST.getlist('local')
        print(len(dias_e_turnos))
        dias_da_semana = []
        turnos = []
        locais2 = []

        for i in range(len(dias_e_turnos)):
            print("for",i)
            dias_da_semana.append(dias_e_turnos[i].split(" ")[0])
            turnos.append(dias_e_turnos[i].split(" ")[1])
            if i!=0 and dias_da_semana[i] == dias_da_semana[i-1]:
                print("dia repetido",i)
                locais2.append(locais1[i-1])
            else:
                locais2.append(locais1[i])
            
            diasNovos = dias(dia=dias_da_semana[i], turno=turnos[i], lugar=locais2[i], id_projeto=projetoNovo)
            diasNovos.save()

        '''
        dias_e_turnos = request.POST.getlist('schedule')
        locais = request.POST.getlist('local')
        j = 0
        for i in dias_e_turnos:
            dias_da_semana = i.split(" ")[0]
            turno = i.split(" ")[1]
            local = locais[j]
            j = j + 1
            diasNovos = dias(dia=dias_da_semana, turno=turno, lugar=local, id_projeto=projetoNovo)
            diasNovos.save()
            print(j,dias_da_semana)
        print("dias",dias)'''
        return redirect('/')
    return render(request, 'create.html')

def projectUpdate(request, projectId):
    if request.method == "POST":
        titulo = request.POST.get('project-name')
        proposta = request.POST.get('proposal')
        curso = request.POST.get('degree')
        coordenador = request.POST.get('professor-name')
        ch_total = request.POST.get('total-hours')
        ch_docente = request.POST.get('weekly-hours-professor')
        ch_estudante = request.POST.get('weekly-hours-student')
        data_inicio = request.POST.get('start-date')
        data_termino = request.POST.get('end-date')
        insta = request.POST.get('instagram')
        contato = request.POST.get('contact')
        form = request.POST.get('formulary')
        aceitando = request.POST.get('availability')
        days = request.POST.get('schedule')
        local = request.POST.get('local')
        disponibilidade = True
        if aceitando == 'off':
            disponibilidade = False
        
        try:
            project = projeto.objects.all().get(id=projectId)
            project.titulo=titulo
            project.proposta=proposta
            project.curso=curso
            project.coordenador=coordenador
            project.ch_total=ch_total
            project.ch_semanal_docente=ch_docente
            project.ch_semanal_estudante=ch_estudante
            project.data_inicio=data_inicio
            project.data_termino=data_termino
            project.instagram=insta
            project.contato=contato
            project.form=form
            project.aceitando=disponibilidade
            project.save()
        except projeto.DoesNotExist:
            raise Http404("Projeto não encontrado.")
        
        try:
            d = dias.objects.all().get(id=projectId)
            diasSemana = days.split(" ")[0]
            turnos = days.split(" ")[1]
            
            for i in range(len(days)):
                d.turno = turnos[i]
                if diasSemana[i] != dias[i+1]:
                    d.dia=diasSemana[i]
                    d.lugar=local[i]
            
            d.save()
        except dias.DoesNotExist:
            pass
    return (request)        