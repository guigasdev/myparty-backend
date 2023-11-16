from django.urls import path
from mypartyApp import views



urlpatterns = [
    path(r'^client$', views.clientsApi),
    path(r'^client/([0,9]+)', )
]