from rest_framework.permissions import BasePermission
from ..models import Classroom


class ClassTeacherOrReadOnly(BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_permission(self, request, view):
        user = request.user
        if request.method == "GET":
            return True

        if request.method == "POST" or request.method == "PUT" or request.method == "DELETE":
            if user.user_profession == "TEACHER":
                return True
        return False


class AssignmentOwnerOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        user = request.user
        if request.method == "GET":
            return True

        if request.method == "POST" or request.method == "PUT" or request.method == "DELETE":
            if user.user_profession == "TEACHER" :
                return True
        return False


class AssignedStudentsOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if request.method == "GET":
            return True

        if request.method == "POST" or request.method == "PUT" or request.method == "DELETE":
            if user.user_profession == "STUDENT":
                return True
        return False


class NoticeCreatorOrReadOnly(BasePermission):
    pass