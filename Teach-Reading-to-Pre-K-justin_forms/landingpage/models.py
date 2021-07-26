from django.db import models
from django.forms import ModelForm
from django import forms
# Create your models here.

class DateInput(forms.DateInput):
    input_type = 'date'

class RiskFactor(models.Model):
    students_First_Name = models.CharField(max_length=30)
    students_Middle_Name = models.CharField(max_length=30)
    students_Last_Name = models.CharField(max_length=30)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    birthdate = models.DateField()
    administration_Date = models.DateField()
    age = models.IntegerField()
    GRADE_CHOICES = (
        ('PK', 'Pre-K'),
        ('K', 'Kindergarten'),
        ('1', '1'),
        ('2', '2'),
    )
    grade = models.CharField(max_length=2, choices=GRADE_CHOICES)
    YN_CHOICES = (('Y', 'Yes'), ('N', 'No'))
    is_English_the_main_language_spoken_at_home = models.CharField(max_length=1, choices=YN_CHOICES)
    does_Student_Qualify_for_Free_or_Reduced_Price_Lunch = models.CharField(max_length=1, choices=YN_CHOICES)
    has_Student_Attended_a_Preschool_Program_or_Head_Start_for_at_least_6_months_in_Same_City_as_Present_School = models.CharField(max_length=1, choices=YN_CHOICES)
    pre_School_Attended = models.CharField(max_length=100)
    ETHNIC_CHOICES = (('C', 'Caucasian'),
                      ('AA', 'African-American'),
                      ('H', 'Hispanic'),
                      ('CI', 'Carribean Island'),
                      ('A', 'Asian'),
                      ('NA', 'Native American'),
                      ('O', 'Other'))
    ethnic_Background_of_person_completing_this = models.CharField(max_length=2, choices=ETHNIC_CHOICES)
    EDU_CHOICES = (('8', 'Less than 8th grade'),
                      ('HS', 'High School'),
                      ('SC', 'Some college'),
                      ('C', 'College'),
                      ('PC', 'Post-college'))
    highest_level_of_education_by_person_completing_this_form = models.CharField(max_length=2, choices=EDU_CHOICES)
    YNO_CHOICES = (('Y', 'Yes'),
                   ('N', 'No'),
                   ('O', 'Do not know'),)
    has_your_child_lived_in_a_house_or_apartment_building_that_was_built_before_1978_for_more_than_6_months = models.CharField(max_length=2, choices=YNO_CHOICES)




class RiskFactorForm(ModelForm):
    class Meta:
        model = RiskFactor
        widgets = {'birthdate' : DateInput(), 'administration_Date' : DateInput()}
        fields = ['students_First_Name',
                  'students_Middle_Name',
                  'students_Last_Name',
                  'gender',
                  'birthdate',
                  'administration_Date',
                  'age',
                  'grade',
                  ]

class q2Form(ModelForm):
    class Meta:
        model = RiskFactor
        fields = ['is_English_the_main_language_spoken_at_home']

class q3Form(ModelForm):
    class Meta:
        model = RiskFactor
        fields = ['does_Student_Qualify_for_Free_or_Reduced_Price_Lunch']

class q4Form(ModelForm):
    class Meta:
        model = RiskFactor
        fields = ['has_Student_Attended_a_Preschool_Program_or_Head_Start_for_at_least_6_months_in_Same_City_as_Present_School',
                  'pre_School_Attended']

class q5Form(ModelForm):
    class Meta:
        model = RiskFactor
        fields = ['ethnic_Background_of_person_completing_this']

class q6Form(ModelForm):
    class Meta:
        model = RiskFactor
        fields = ['highest_level_of_education_by_person_completing_this_form']

class q7Form(ModelForm):
    class Meta:
        model = RiskFactor
        fields = ['has_your_child_lived_in_a_house_or_apartment_building_that_was_built_before_1978_for_more_than_6_months']
