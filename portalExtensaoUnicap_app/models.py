from django.db import models
from django.templatetags.static import static

class projeto(models.Model):
    id=models.BigAutoField(primary_key=True);

    identificacao_unica=models.TextField();
    titulo=models.TextField();
    proposta=models.TextField();
    curso=models.TextField();
    coordenador=models.TextField();

    ch_total=models.IntegerField();
    ch_semanal_docente=models.IntegerField();
    ch_semanal_estudante=models.IntegerField();

    data_inicio=models.DateField();
    data_termino=models.DateField();

    instagram=models.TextField();
    contato=models.TextField();
    formulario=models.TextField();

    #imagem
    def image_url(projeto):
        file_name = f"{projeto.nome}.png" #???
        image_path = f"graphics/img_projeto/{file_name}"
        return static(image_path)


class dias(models.Model):
    id=models.BigAutoField(primary_key=True);
    id_projeto=models.ForeignKey('projeto', on_delete=models.CASCADE)

    dia=models.IntegerField(); # 1==dom, 2==seg, etc, 7==sab
    turno=models.IntegerField(); # 1==dia, 2==tarde, 3==noite
    lugar=models.TextField();


class areas(models.Model):
    id=models.BigAutoField(primary_key=True);
    id_projeto=models.ForeignKey('projeto', on_delete=models.CASCADE)
    area=models.TextField();


class adm(models.Model):
    id=models.BigAutoField(primary_key=True);
    email=models.TextField();
    senha=models.TextField();
