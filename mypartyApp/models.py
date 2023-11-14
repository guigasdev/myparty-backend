from django.db import models

# Create your models here.

class clients(models.Model):
    clientId = models.AutoField(primary_key=True)
    clientName = models.CharField(max_length=30)



class events(models.Model):
    eventId = models.AutoField(primary_key=True)
    eventName = models.CharField(max_length=500)
    

