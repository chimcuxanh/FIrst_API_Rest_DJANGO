from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializers
from .models import Task


@api_view(['GET'])
def apioverview(request):
    api_url = {
        'List': '/task-list/',
        'Detail-view': '/task-detail/<str:pk>/',
        'Create': '/task-create/',
        'Update': '/task-update/<str:pk>/',
        'Delete': '/task-delete/<str:pk>/',
    }
    return Response(api_url)


@api_view(['GET'])
def task_list(request):
    tasks = Task.objects.all()
    serializer = TaskSerializers(tasks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def task_detail(request, pk):
    tasks = Task.objects.get(id=pk)
    serializer = TaskSerializers(tasks, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def task_create(request):
    serializers = TaskSerializers(data=request.data)

    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)

@api_view(['POST'])
def task_update(request, pk):
    tasks = Task.objects.get(id=pk)
    serializers = TaskSerializers(instance=tasks, many=True)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)

@api_view(['DELETE'])
def task_delete(request, pk):
    tasks = Task.objects.get(id=pk)
    tasks.delete()
    return Response("item deleted")