from django.contrib import admin
from .models import User, Teacher, Student, Classroom, CreatedAssignment, CompletedAssignment, Notice

admin.site.register(User)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Classroom)
admin.site.register(CreatedAssignment)
admin.site.register(CompletedAssignment)
admin.site.register(Notice)

