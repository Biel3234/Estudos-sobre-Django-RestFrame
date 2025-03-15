from django.shortcuts import render
from .models import Usuario
from .serializers import SerializadorUsuario

import requests

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view (['GET', 'POST'])
def create_list(request):
    if request.method == 'GET':
        usuarios = Usuario.objects.all()
        serializer = SerializadorUsuario(usuarios, many = True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = SerializadorUsuario(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view (['GET', 'PUT', 'DELETE'])
def detail_delete_edit(request, pk):
    try:
        usuario = Usuario.objects.get(pk = pk)
    except Usuario.DoesNotExist:
        return Response({'error': 'Nao encontrado'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = SerializadorUsuario(usuario)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = SerializadorUsuario(usuario, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        usuario.delete()
        return Response({'message': 'Usuário deletado'}, status=status.HTTP_204_NO_CONTENT)
