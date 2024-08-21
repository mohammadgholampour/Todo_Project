from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')  

def index(request):
    return render(request, 'frontend/index.html')  


class TaskListCreate(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
