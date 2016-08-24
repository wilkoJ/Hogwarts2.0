from django.contrib import admin

from .models import Teacher, Course, Student, House

class TeacherAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,{'fields': ['teacher_name']}),
        ('Course teached',{'fields':['course_teached']}),
    ]
class HouseAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,{'fields': ['house_name']}),
        ('House students',{'fields':['house_students']}),
    ]
class StudentAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,{'fields': ['student_name']}),
        ('Student points',{'fields':['points']}),
    ]
class CourseAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,{'fields': ['course_name']}),
        ('Course students',{'fields':['course_students']}),
    ]
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(House, HouseAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Course, CourseAdmin)
