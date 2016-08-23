Data Model Hogwarts Project:

Class Teacher:
   Course course
 method:
   grade_student(Int student_id, Char grade)
   give_points(Int student_id, Int nb_points)
   retrieve_points(Int student_id, Int nb_points) //might refactories this one with give_point(student_id, -nb_point).

Class Course
   Int class_id
   Student students[]
 method:
   add_student()
  
Class House:
   Student students[] = student_lsit
   Int houses_point;
 method:
   count_points()

Class Student:
   Int student_id
   Int points
   Course courses[]
 method:
   join_class(Course course)


This is the model i would imagine at first it might change as and when the project advance.

