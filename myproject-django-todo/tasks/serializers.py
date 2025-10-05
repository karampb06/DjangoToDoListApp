#-*- coding:utf-8 -*-
from rest_framework import serializers
from .models import Task, Status
 
 
class TaskSerializer(serializers.ModelSerializer):
    """
    Serializer for Task model - handles all CRUD operations
    """
    status_display = serializers.CharField(source='get_status_display', read_only=True)
    class Meta:
        model = Task
        fields = ['id', 'name', 'status', 'status_display']
        read_only_fields = ['id']
    def validate_name(self, value):
        """
        Check that task name is not empty and has reasonable length
        """
        if not value.strip():
            raise serializers.ValidationError("Task name cannot be empty.")
        return value.strip()
 
 
class TaskCreateSerializer(serializers.ModelSerializer):
    """
    Specialized serializer for creating tasks
    """
    class Meta:
        model = Task
        fields = ['name', 'status']
    def validate_name(self, value):
        """
        Check that task name is not empty and has reasonable length
        """
        if not value.strip():
            raise serializers.ValidationError("Task name cannot be empty.")
        return value.strip()
    def validate_status(self, value):
        """
        Ensure status is valid
        """
        if value not in [choice[0] for choice in Status.choices]:
            raise serializers.ValidationError("Invalid status choice.")
        return value
 
 
class TaskUpdateSerializer(serializers.ModelSerializer):
    """
    Specialized serializer for updating tasks
    """
    class Meta:
        model = Task
        fields = ['name', 'status']
    def validate_name(self, value):
        """
        Check that task name is not empty and has reasonable length
        """
        if not value.strip():
            raise serializers.ValidationError("Task name cannot be empty.")
        return value.strip()
    def validate_status(self, value):
        """
        Ensure status is valid
        """
        if value not in [choice[0] for choice in Status.choices]:
            raise serializers.ValidationError("Invalid status choice.")
        return value
 
 
class TaskListSerializer(serializers.ModelSerializer):
    """
    Lightweight serializer for listing tasks
    """
    status_display = serializers.CharField(source='get_status_display', read_only=True)
    class Meta:
        model = Task
        fields = ['id', 'name', 'status', 'status_display']
 
 
class TaskDetailSerializer(serializers.ModelSerializer):
    """
    Detailed serializer for retrieving single task
    """
    status_display = serializers.CharField(source='get_status_display', read_only=True)
    class Meta:
        model = Task
        fields = ['id', 'name', 'status', 'status_display']