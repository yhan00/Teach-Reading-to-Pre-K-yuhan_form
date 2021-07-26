from django.urls import path
from . import views

app_name = "exam"

urlpatterns = [path('q1/', views.q1, name='q1'),
               path('q2/', views.q2, name='q2'),
               path('q3/', views.q3, name='q3'),
               path('q4/', views.q4, name='q4'),
               path('q5/', views.q5, name='q5'),
               path('q6/', views.q6, name='q6'),
               path('q7/', views.q7, name='q7'),
               path('q8/', views.q8, name='q8'),
               path('q9/', views.q9, name='q9'),
               path('q10/', views.q10, name='q10'),
               path('q11/', views.q11, name='q11'),
               path('q12/', views.q12, name='q12'),
               path('q13/', views.q13, name='q13'),
               path('q14/', views.q14, name='q14'),
               path('q15/', views.q15, name='q15'),
               path('q16/', views.q16, name='q16'),
               path('q17/', views.q17, name='q17'),]