from django.shortcuts import render
from rest_framework import viewsets
from .models import Todo
from .serializers import TodoSerializer, TodoListSerializer
from rest_framework.response import Response
# Create your views here.

class TodoViewset(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer



    def list(self, request, *args, **kwargs):
        todos = Todo.objects.all()
        serializer = TodoListSerializer(todos,many=True)
        return Response (serializer.data)


class TodoViewset(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer



    def list(self, request, *args, **kwargs):
        todos = Todo.objects.all()
        serializer = TodoListSerializer(todos,many=True)
        return Response (serializer.data)