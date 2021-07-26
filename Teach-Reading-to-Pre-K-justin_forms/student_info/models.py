from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import fields
from django.forms import ModelForm
from django.contrib.auth.models import User
# Create your models here.

class Classroom(models.Model):
    name = models.CharField(max_length=30)
    grade = models.CharField(max_length=4)
    # teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    average_at_risk = models.IntegerField(null=False, blank=True, default=0)


class ClassroomForm(ModelForm):
    class Meta:
        model = Classroom
        fields = ['name', 'grade']


class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    # age = models.IntegerField()
    date_of_birth = models.DateField()
    grade = models.CharField(max_length=4)
    # teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    # Test Related
    QUESTION_CHOICES = (
        ('Y', 'Correct Answer'),
        ('N', 'Incorrect Answer')
    )
    question_1 = models.CharField(max_length=1, choices=QUESTION_CHOICES, default='N')
    question_2 = models.CharField(max_length=1, choices=QUESTION_CHOICES, default='N')
    question_3 = models.CharField(max_length=1, choices=QUESTION_CHOICES, default='N')
    question_4 = models.CharField(max_length=1, choices=QUESTION_CHOICES, default='N')
    question_5 = models.CharField(max_length=1, choices=QUESTION_CHOICES, default='N')
    question_6 = models.CharField(max_length=1, choices=QUESTION_CHOICES, default='N')
    question_7 = models.CharField(max_length=1, choices=QUESTION_CHOICES, default='N')
    question_8 = models.CharField(max_length=1, choices=QUESTION_CHOICES, default='N')
    question_9 = models.CharField(max_length=1, choices=QUESTION_CHOICES, default='N')
    question_10 = models.CharField(max_length=1, choices=QUESTION_CHOICES, default='N')
    question_11 = models.CharField(max_length=1, choices=QUESTION_CHOICES, default='N')
    question_12 = models.CharField(max_length=1, choices=QUESTION_CHOICES, default='N')
    question_13 = models.CharField(max_length=1, choices=QUESTION_CHOICES, default='N')
    question_14 = models.CharField(max_length=1, choices=QUESTION_CHOICES, default='N')
    question_15 = models.CharField(max_length=1, choices=QUESTION_CHOICES, default='N')
    question_16 = models.CharField(max_length=1, choices=QUESTION_CHOICES, default='N')
    question_17 = models.CharField(max_length=1, choices=QUESTION_CHOICES, default='N')

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'date_of_birth', 'grade', 'classroom', 'gender']




