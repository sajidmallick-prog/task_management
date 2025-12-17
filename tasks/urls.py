from django.urls import path 
from tasks.views import TaskListCreateView, TaskDetailView

urlpatterns = [
    # Tasks 
    path('tasks/', TaskListCreateView.as_view(), name='task-list'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
]