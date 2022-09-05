from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import ClassroomSerializer, CreatedAssignmentSerializer, CompletedAssignmentSerializer, NoticeSerializer
from .models import Classroom, CreatedAssignment, CompletedAssignment, Notice
from .permissions.myclassroom_permission import ClassTeacherOrReadOnly, AssignmentOwnerOrReadOnly, AssignedStudentsOrReadOnly




class ClassroomViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, ClassTeacherOrReadOnly]
    authentication_classes = [BasicAuthentication]
    serializer_class = ClassroomSerializer
    queryset = Classroom.objects.all()
    
    

class CreatedAssignmentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, AssignmentOwnerOrReadOnly]
    authentication_classes = [BasicAuthentication]
    serializer_class = CreatedAssignmentSerializer
    queryset = CreatedAssignment.objects.all()
    
    

class CompletedAssignmentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, AssignedStudentsOrReadOnly]
    authentication_classes = [BasicAuthentication]
    serializer_class = CompletedAssignmentSerializer
    queryset = CompletedAssignment.objects.all()


class NoticeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, AssignmentOwnerOrReadOnly]
    authentication_classes = [BasicAuthentication]
    serializer_class = NoticeSerializer
    queryset = Notice.objects.all()
