from rest_framework import serializers
from .models import Usuario

class SerializadorUsuario(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        
        fields = ['id', 'nome', 'idade', 'mensagem']