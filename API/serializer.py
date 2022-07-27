from dataclasses import field
from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers

from .models import  *


class ImagenesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imagenes;
        fields = '__all__'

class VideosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Videos;
        fields = '__all__'

class InvitadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invitado;
        #fields = ('id','ApellidoP','ApellidoM','nombre','semestre','id_carrera')
        fields = '__all__'
      
    def to_representation(self, instance):
        return {
            'id': instance.id,
            'correo': instance.correo,
            'genero': instance.genero,
            'edad': instance.edad,
            'salario': instance.salario,
            'mac': instance.mac,
        }