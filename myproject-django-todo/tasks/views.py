from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
 
from .models import Task
from .forms import TaskForm
from .serializers import (
    TaskSerializer, 
    TaskCreateSerializer, 
    TaskUpdateSerializer, 
    TaskListSerializer, 
    TaskDetailSerializer
)
# ========================
# REST API CLASS-BASED VIEWS

# Create your views here.
# Functional based view
# Create a task
# def task_create(request):
#     if request.method == "POST":
#         form = TaskForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(reverse("tasks:task_list"))
#     else:
#         form = TaskForm()
#
#     return render(request, "tasks/task_form.html", { "form": form, })
#
#
# # Retrieve task list
# def task_list(request):
#     tasks = Task.objects.all()
#     return render(request, "tasks/task_list.html", { "tasks": tasks,})
#
#
# # Retrieve a single task
# def task_detail(request, pk):
#     task = get_object_or_404(Task, pk=pk)
#     return render(request, "tasks/task_detail.html", { "task": task, })
#
#
# # Update a single task
# def task_update(request, pk):
#     task_obj = get_object_or_404(Task, pk=pk)
#     if request.method == 'POST':
#         form = TaskForm(instance=task_obj, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(reverse("tasks:task_detail", args=[pk,]))
#     else:
#         form = TaskForm(instance=task_obj)
#
#     return render(request, "tasks/task_form.html", { "form": form, "object": task_obj})
#
#
# # Delete a single task
# def task_delete(request, pk):
#     task_obj = get_object_or_404(Task, pk=pk)
#     task_obj.delete()
#     return redirect(reverse("tasks:task_list"))

# Class Based Views

'''

from django.views.generic import ListView, DetailView, \
    CreateView, UpdateView, DeleteView

class TaskListView(ListView):
    model = Task
    context_object_name = 'tasks'

class TaskDetailView(DetailView):
    model = Task

class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('tasks:task_list')

class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('tasks:task_list')

class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy('tasks:task_list')
'''
# ========================
# REST API CLASS-BASED VIEWS
# ========================
 
class TaskListCreateAPIView(generics.ListCreateAPIView):
    """
    API endpoint for listing all tasks and creating new tasks.
    GET /api/tasks/ - List all tasks
    POST /api/tasks/ - Create a new task
    """
    queryset = Task.objects.all()
    authentication_classes = [JWTAuthentication, BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TaskCreateSerializer
        return TaskListSerializer
    def get_queryset(self):
        """
        Optionally filter tasks by status via query parameter
        Example: /api/tasks/?status=u (for unstarted tasks)
        """
        queryset = Task.objects.all().order_by('-id')
        status_param = self.request.query_params.get('status', None)
        if status_param is not None:
            queryset = queryset.filter(status=status_param)
        return queryset
 
 
class TaskDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint for retrieving, updating, and deleting a specific task.
    GET /api/tasks/{id}/ - Retrieve a specific task
    PUT /api/tasks/{id}/ - Update a specific task (full update)
    PATCH /api/tasks/{id}/ - Partially update a specific task
    DELETE /api/tasks/{id}/ - Delete a specific task
    """
    queryset = Task.objects.all()
    authentication_classes = [JWTAuthentication, BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return TaskUpdateSerializer
        return TaskDetailSerializer
 
 
class TaskListAPIView(generics.ListAPIView):
    """
    API endpoint for listing all tasks (read-only).
    GET /api/tasks/list/ - List all tasks
    """
    queryset = Task.objects.all().order_by('-id')
    serializer_class = TaskListSerializer
    authentication_classes = [JWTAuthentication, BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        """
        Optionally filter tasks by status via query parameter
        Example: /api/tasks/list/?status=u (for unstarted tasks)
        """
        queryset = Task.objects.all().order_by('-id')
        status_param = self.request.query_params.get('status', None)
        if status_param is not None:
            queryset = queryset.filter(status=status_param)
        return queryset
 
 
class TaskCreateAPIView(generics.CreateAPIView):
    """
    API endpoint for creating new tasks.
    POST /api/tasks/create/ - Create a new task
    """
    queryset = Task.objects.all()
    serializer_class = TaskCreateSerializer
    authentication_classes = [JWTAuthentication, BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
 
 
class TaskUpdateAPIView(generics.UpdateAPIView):
    """
    API endpoint for updating existing tasks.
    PUT /api/tasks/{id}/update/ - Update a specific task (full update)
    PATCH /api/tasks/{id}/update/ - Partially update a specific task
    """
    queryset = Task.objects.all()
    serializer_class = TaskUpdateSerializer
    authentication_classes = [JWTAuthentication, BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
 
 
class TaskDeleteAPIView(generics.DestroyAPIView):
    """
    API endpoint for deleting tasks.
    DELETE /api/tasks/{id}/delete/ - Delete a specific task
    """
    queryset = Task.objects.all()
    authentication_classes = [JWTAuthentication, BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            {'message': f'Task "{instance.name}" has been deleted successfully.'}, 
            status=status.HTTP_200_OK
        )