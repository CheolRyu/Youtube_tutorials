''' we added serializers to view a specific data in our models. 
    Therefore, I imported serializers from rest frame work'''
from rest_framework import serializers

''' also imported the models from model '''
from .models import *


class TaskSerializer(serializers.ModelSerializer):
  ''' for our sake of using the same name as model Task,  
      I gave a name as TaskSerializer. Also, in order for this class to work
      we need two attributes in the meta class, the model that we want, 
      and how many fields we want to show.'''
      
  class Meta:
    model = Task
    fields = '__all__'