from django.urls import path
from .views import TaskListCreate
from .views import TaskListCreate, index

urlpatterns = [
    path('tasks/', TaskListCreate.as_view(), name='task-list-create'),
    path('', index, name='index'),
]
