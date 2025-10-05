#-*- coding:utf-8 -*-
 
from django.urls import path, re_path
from . import views
 
# namespace
app_name = 'tasks'
 
urlpatterns = [
    # Combined List and Create endpoint
    path('', views.TaskListCreateAPIView.as_view(), name='task-list-create'),
    # Individual task operations (retrieve, update, delete)
    path('<int:pk>/', views.TaskDetailAPIView.as_view(), name='task-detail'),
    # Separate endpoints for specific operations (alternative routes)
    path('list/', views.TaskListAPIView.as_view(), name='task-list'),
 
    path('create/', views.TaskCreateAPIView.as_view(), name='task-create'),
 
    path('<int:pk>/update/', views.TaskUpdateAPIView.as_view(), name='task-update'),
    path('<int:pk>/delete/', views.TaskDeleteAPIView.as_view(), name='task-delete'),
    # OLD URL PATTERNS (COMMENTED OUT - KEEPING FOR REFERENCE)
    # # Create a task
    # path('create/', views.TaskCreateView.as_view(), name='task_create'),
    # # Retrieve task list
    # path('', views.TaskListView.as_view(), name='task_list'),
    # # Retrieve single task object
    # re_path(r'^(?P<pk>\d+)/$', views.TaskDetailView.as_view(), name='task_detail'),
    # # Update a task
    # re_path(r'^(?P<pk>\d+)/update/$', views.TaskUpdateView.as_view(), name='task_update'),
    # # Delete a task
    # re_path(r'^(?P<pk>\d+)/delete/$', views.TaskDeleteView.as_view(), name='task_delete')
 
    # # Create a task
    # path('create/', views.task_create, name='task_create'),
    # # Retrieve task list
    # path('', views.task_list, name='task_list'),
    # # Retrieve single task object
    # re_path(r'^(?P<pk>\d+)/$', views.task_detail, name='task_detail'),
    # # Update a task
    # re_path(r'^(?P<pk>\d+)/update/$', views.task_update, name='task_update'),
    # # Delete a task
    # re_path(r'^(?P<pk>\d+)/delete/$', views.task_delete, name='task_delete'),
 
]