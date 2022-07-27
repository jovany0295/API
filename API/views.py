from django.shortcuts import render
from django.urls import *
from rest_framework import viewsets
from .models import *
from .serializer import  *

# Create your views here.
class ImagenesViewSet(viewsets.ModelViewSet):
    queryset = Imagenes.objects.all().order_by('id')
    serializer_class = ImagenesSerializer

class VideosViewSet(viewsets.ModelViewSet):
    queryset = Videos.objects.all().order_by('id')
    serializer_class = VideosSerializer   
class InvitadoViewSet(viewsets.ModelViewSet):
    queryset = Invitado.objects.all().order_by('id')
    serializer_class = InvitadoSerializer
