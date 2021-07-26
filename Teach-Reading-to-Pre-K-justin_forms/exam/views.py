from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render
from student_info.models import Student

# Create your views here.

def q1(request):
    print("PK:")
    return render(request, 'q1.html')
def q2(request):
    return render(request, 'q2.html')
def q3(request):
    return render(request, 'q3.html')
def q4(request):
    return render(request, 'q4.html')
def q5(request):
    return render(request, 'q5.html')
def q6(request):
    return render(request, 'q6.html')
def q7(request):
    return render(request, 'q7.html')
def q8(request):
    return render(request, 'q8.html')
def q9(request):
    return render(request, 'q9.html')
def q10(request):
    return render(request, 'q10.html')
def q11(request):
    return render(request, 'q11.html')
def q12(request):
    return render(request, 'q12.html')
def q13(request):
    return render(request, 'q13.html')
def q14(request):
    return render(request, 'q14.html')
def q15(request):
    return render(request, 'q15.html')
def q16(request):
    return render(request, 'q16.html')
def q17(request):
    return render(request, 'q17.html')

def upd_q1(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.question_1 = 'Y'
    student.save(update_fields=['question_1'])
    return redirect('q2')

def upd_q2(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.question_2 = 'Y'
    student.save(update_fields=['question_2'])
    return redirect('q3')

def upd_q3(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.question_3 = 'Y'
    student.save(update_fields=['question_3'])
    return redirect('q4')

def upd_q4(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.question_4 = 'Y'
    student.save(update_fields=['question_4'])
    return redirect('q5')

def upd_q5(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.question_5 = 'Y'
    student.save(update_fields=['question_5'])
    return redirect('q6')

def upd_q6(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.question_6 = 'Y'
    student.save(update_fields=['question_6'])
    return redirect('q7')

def upd_q7(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.question_7 = 'Y'
    student.save(update_fields=['question_7'])
    return redirect('q8')

def upd_q8(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.question_8 = 'Y'
    student.save(update_fields=['question_8'])
    return redirect('q9')

def upd_q9(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.question_9 = 'Y'
    student.save(update_fields=['question_9'])
    return redirect('q10')

def upd_q10(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.question_10 = 'Y'
    student.save(update_fields=['question_10'])
    return redirect('q11')

def upd_q11(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.question_11 = 'Y'
    student.save(update_fields=['question_11'])
    return redirect('q12')

def upd_q12(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.question_12 = 'Y'
    student.save(update_fields=['question_12'])
    return redirect('q13')

def upd_q13(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.question_13 = 'Y'
    student.save(update_fields=['question_13'])
    return redirect('q14')

def upd_q14(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.question_14 = 'Y'
    student.save(update_fields=['question_14'])
    return redirect('q15')

def upd_q15(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.question_15 = 'Y'
    student.save(update_fields=['question_15'])
    return redirect('q16')

def upd_q16(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.question_16 = 'Y'
    student.save(update_fields=['question_16'])
    return redirect('q17')

def upd_q17(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.question_17 = 'Y'
    student.save(update_fields=['question_17'])
    return redirect('idk')