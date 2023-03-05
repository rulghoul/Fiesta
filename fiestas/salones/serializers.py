from .models import TipoActividad, TipoEvento, TipoServicio
from rest_framework import serializers


class ActividadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TipoActividad
        fields = ['clave', 'descripcion']


class EventoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TipoEvento
        fields =  ['clave', 'descripcion']

class ServicioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TipoServicio
        fields =  ['clave', 'descripcion']

