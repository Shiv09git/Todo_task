from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.ModelSerializer ):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'description', 'is_completed', 'date')


class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'date', 'is_completed')