from django.contrib.auth.models import User
from django.shortcuts import render
from .models import Student, StudentForm, ClassroomForm
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
def createStudent(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        else:
            messages.info(request, 'Could not create new student. Try again.')
            return redirect("student_info:student_form")
    else:
        form = StudentForm()
    return render(request, 'student_form.html', {'form':form})


def createClassroom(request):
    if request.method == 'POST':
        form = ClassroomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        else:
            messages.info(request, 'Could not create new student. Try again.')
            return redirect("student_info:classroom_form")
    else:
        form = ClassroomForm()
    return render(request, 'classroom_form.html', {'form':form})


def students(request):
    studentList = Student.objects.all()
    return render(request, 'students.html', {'students': studentList})