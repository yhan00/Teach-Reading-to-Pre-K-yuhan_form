from django.urls import path
from . import views

app_name = "student_info"

urlpatterns = [
    path('students', views.students, name='students'),
    path('student_form', views.createStudent, name='student_form'),
    path('classroom_form', views.createClassroom, name='classroom_form'),
]