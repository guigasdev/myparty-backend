from django.db import models

# Create your models here.

class clients(models.Model):
    clientId = models.AutoField(primary_key=True)
    clientName = models.CharField(max_length=30)
    clientPass = models.TextField(max_length=500, default='DEFAULT VALUE')
    clientEmail = models.EmailField(max_length=500, default='DEFAULT VALUE')
    clientNumber = models.TextField(max_length=500, default='DEFAULT VALUE')
    clientCPF = models.TextField(max_length=500, default='DEFAULT VALUE')

    
class events(models.Model):
    eventId = models.AutoField(primary_key=True)
    eventName = models.CharField(max_length=500)
    eventInicio = models.TextField(max_length=500, default='DEFAULT VALUE')
    eventFim = models.TextField(max_length=500, default='DEFAULT VALUE')
    eventLocal = models.TextField(max_length=500, default='DEFAULT VALUE')
    eventCEP = models.TextField(max_length=500, default='DEFAULT VALUE')
    eventProdutor = models.TextField(max_length=500, default='DEFAULT VALUE')
