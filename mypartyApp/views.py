from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from mypartyApp.models import clients,events
from mypartyApp.serializers import clientsSerializer, eventsSerializer


# Create your views here.

@csrf_exempt
def clientsApi(request, id=0):
    if request.method == 'GET':
        clients = clients.object.all()
        clients_serializer = clientsSerializer(clients, many=True)
        return JsonResponse(clients_serializer.data, safe=False)
    elif request.method == 'POST':
        clients_data = JSONParser().parse(request)
        clients_serializer = clients_serializer(data = clients_data)
        if clients_serializer.is_valid():
            clients_serializer.save()
            return JsonResponse("Adicionado com sucesso", safe=False)
        return JsonResponse('Falha ao adiconar', safe=False)
    elif request.method == 'PUT':
        client_data = JSONParser().parse(request)
        client = clients.objects.get(clientId=client_data['clientId']) 
        clients_serializer = clientsSerializer(client, data=client_data)
        if clients_serializer.is_valid():
            clients_serializer.save()
            return JsonResponse("O carregamento foi feito com sucesso!", safe=False)
        return JsonResponse("Falha ao carregar")
    elif request.method == 'DELETE':
        client = clients.objects.get(clientId=id)
        client.delete()
        return JsonResponse("Deletado com sucesso", safe=False)
    
