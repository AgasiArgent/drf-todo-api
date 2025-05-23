from django.shortcuts import render

from rest_framework import viewsets, filters
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset         = Task.objects.order_by('-created_at')
    serializer_class = TaskSerializer
    filter_backends  = [filters.SearchFilter]
    search_fields    = ['completed']
