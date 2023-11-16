from rest_framework import serializers
from mypartyApp.models import clients, events

class clientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = clients
        fields = ('clientId', 'clientName', 'clientPass', 'clientEmail', 'clientPass', 'clientNumber', 'clientCPF' )

class eventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = events
        fields = ('eventId', 'eventName', 'eventInicio', 'eventFim', 'eventLocal', 'eventCEP', 'eventProdutor' )
        