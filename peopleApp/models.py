from datetime import datetime
from tkinter import CASCADE
from django.db import models

# Create your models here.
class People( models.Model):
  nome_completo = models.CharField(max_length=256)
  data_nascimento = models.DateField(null=True)
  ativa = models.BooleanField(default=True)

  def __str__(self):
    return self.data_nascimento
  
  def __str__(self):
    return self.nome_completo

class Contato (models.Model): 
  nome = models.CharField(max_length=200)
  email = models.EmailField(max_length=200)
  telefone = models.CharField(max_length=200) 
  pessoa = models.ForeignKey(People, on_delete = models.CASCADE) 

  def __str__(self): 
    return self.nome