from django.db import models
from django.templatetags.static import static
from django.core.validators import MinValueValidator, MaxValueValidator

class projeto(models.Model):
    id=models.BigAutoField(primary_key=True)

    identificacao_unica=models.TextField(max_length=9, blank=False, null=False)
    titulo=models.TextField(max_length=300, blank=False, null=False)
    proposta=models.TextField(max_length=3000, blank=False, null=False)
    curso=models.TextField(max_length=150, blank=False, null=False)
    coordenador=models.TextField(max_length=150, blank=False, null=False)

    ch_total=models.IntegerField(blank=False, null=False)
    ch_semanal_docente=models.IntegerField(blank=False, null=False)
    ch_semanal_estudante=models.IntegerField(blank=False, null=False)

    data_inicio=models.DateField(auto_now=False, auto_now_add=False)
    data_termino=models.DateField(auto_now=False, auto_now_add=False)

    instagram=models.TextField(blank=True)
    contato=models.TextField(blank=False)
    formulario=models.TextField(blank=True)

    #imagem
    def image_url(projeto):
        file_name = f"{projeto.nome}.png" #???
        image_path = f"graphics/img_projeto/{file_name}"
        return static(image_path)


class dias(models.Model):
    id=models.BigAutoField(primary_key=True)
    id_projeto=models.ForeignKey('projeto', on_delete=models.CASCADE)

    dia=models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(7)]); # 1==dom, 2==seg, etc, 7==sab
    turno=models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(3)]); # 1==dia, 2==tarde, 3==noite
    lugar=models.TextField(max_length=300, blank=False, null=False)


class areas(models.Model):
    id=models.BigAutoField(primary_key=True)
    id_projeto=models.ForeignKey('projeto', on_delete=models.CASCADE)
    area=models.TextField(max_length=150, blank=False, null=False)


class adm(models.Model):
    id=models.BigAutoField(primary_key=True)
    email=models.TextField(max_length=150, blank=False, null=False)
    senha=models.TextField(max_length=150, blank=False, null=False)
