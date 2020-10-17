from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import serializers
from .models import *
''' imports api views from frame work decorator '''
from rest_framework.decorators import api_view 

''' imports response from frame work response '''
from rest_framework.response import Response

''' we need to import serializers to use it in this view. '''
from .serializers import TaskSerializer
# Create your views here.

''' this would allow me to use json data becuase we imported the api_views and the response '''
@api_view(['GET'])
def apiOverview(request):
  api_urls = {
    'List': '/task-list/', 
    'Detail View': '/task-detail/<str:pk>', 
    'Create': '/task-create/', 
    'Update': '/task-update/<str:pk>/', 
    'Delete': '/task-delete/<str:pk>/',

  }
  return Response(api_urls)

  ''' Just so that we can see all of the datas in our base
      create a function and return the Response(). Within this function, we fetch data from the model as tasks, 
      then render it to serializer with many attribute, then it would return the serialized data within
      the Response(serializer.data)'''
@api_view(['GET'])
def taskList(request):
  tasks = Task.objects.all() 
  serializer = TaskSerializer(tasks, many=True)
  return Response(serializer.data)
