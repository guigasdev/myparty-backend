from django.db import models

# Create your models here.

class clients(models.Model):
    clientId = models.AutoField(primary_key=True)
    clientName = models.CharField(max_length=30)
    clientEmail = models.EmailField()
    clientNumber = models.CharField()
    clientPasssword = models.CharField()
    clientcpf = models.CharField()
    



class events(models.Model):
    eventId = models.AutoField(primary_key=True)
    eventName = models.CharField(max_length=500)
    eventBeggin =  models.CharField(max_length=500)
    eventEnd =  models.CharField(max_length=500)
    qtd_max = models.CharField(max_length=500)
    cidade  = models.CharField(max_length=500)
    estado = models.CharField(max_length=500)
    cep = models.CharField(max_length=500)
    produtor = models.CharField(max_length=500)