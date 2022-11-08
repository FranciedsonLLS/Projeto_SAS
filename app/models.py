from unittest.util import _MAX_LENGTH
from django.db import models


from customauth.models import MyUser

# Create your models here.

class Rua(models.Model):
    nome =  models.CharField(max_length=75, null=True, blank=True)
    foto = models.TextField(null=True, blank=True)    
    descricao =  models.CharField(max_length=75, null=True, blank=True)
    class Meta:
        verbose_name_plural = "Ruas"
    def __str__(self):
        return str(self.nome)


class Festival(models.Model):
    nome =  models.CharField(max_length=75, null=True, blank=True)
    foto = models.CharField(max_length=400, null=True, blank=True)      
    descricao =  models.CharField(max_length=75, null=True, blank=True)
    rua = models.ForeignKey(Rua, on_delete= models.CASCADE)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)     
    class Meta:
        verbose_name_plural = "Festivais"
    def __str__(self):
        return str(self.nome)

class Participante(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)  
    festival = models.ForeignKey(Festival, on_delete=models.CASCADE)   
    class Meta:
        verbose_name_plural = "Participantes"
    def __str__(self):
        return str(self.nome)



