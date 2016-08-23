from __future__ import unicode_literals

from django.db import models

class Student(models.Model):
    student_id = models.IntegerField(default=0)
    student_name = models.CharField(max_length=30)
    points = models.IntegerField(default=0)
    def __str__(self):
        return self.student_name
    def join_course(self, course):
        course.append(self)

class House(models.Model):
    house_name = models.CharField(max_length=30)
    house_students = models.ManyToManyField(Student)
    house_points = models.IntegerField(default=0)
    def __str__(self):
        return self.house_name
    def count_point():
        house_points = 0
        for student in house_students:
            hourse_points += student.points

class Course(models.Model):
    course_name = models.CharField(max_length=30)
    course_students = models.ManyToManyField(Student);
    def __str__(self):
        return self.course_name
            
class Teacher(models.Model):
    teacher_name = models.CharField(max_length=30)
    course_teached = models.ForeignKey(Course, on_delete=models.CASCADE)
    def __str__(self):
        return self.teacher_name
    def add_points(student, points):
        student.points += points
    def retrieve_points(student, points):
        student.points -= points