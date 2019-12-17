from django.db import models

# Create your models here.

class Postagem(models.Model):
    opcao_tema=[
        ('ROM', 'Roamnce'),
        ('GAM', 'Games'),
        ('PRO', 'Profissão'),
    ]
    nome = models.CharField(max_length=50)
    idade = models.IntegerField(default=1)
    email = models.CharField(max_length=50)
    ativo = models.BooleanField(default=True)
    tema = models.CharField(max_length=3, choices=opcao_tema)
    texto_blog = models.CharField(max_length=150)
    


