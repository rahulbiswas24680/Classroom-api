from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import Classroom, CreatedAssignment, CompletedAssignment, Notice



class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ['id', 'user']



class CompletedAssignmentSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = CompletedAssignment
        fields = ['title', 'url', 'description', 'assignment', 'photo', 'pdffile']
       

class CreatedAssignmentSerializer(serializers.HyperlinkedModelSerializer):
    stored_assignments = CompletedAssignmentSerializer(many=True, read_only=True)
    class Meta:
        model = CreatedAssignment
        fields = ['id', 'url', 'title', 'description', 'stored_assignments', 'completed']
       

class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = '__all__'

