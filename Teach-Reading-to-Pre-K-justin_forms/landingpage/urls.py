from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('riskfactorform', views.riskfactorform, name='riskfactorform'),    path('q2', views.q2form, name='q2'),
    path('dyslexiaform', views.dyslexiaform, name='dyslexiaform'),
    path('q3', views.q3form, name='q3'),
    path('q4', views.q4form, name='q4'),
    path('q5', views.q5form, name='q5'),
    path('q6', views.q6form, name='q6'),
    path('q7', views.q7form, name='q7'),
]