from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .models import RiskFactorForm, q2Form, q3Form, q4Form, q5Form, q6Form, q7Form

def index(request):
    return render(request, 'index.html')

def riskfactorform(request):
    if request.method == 'POST':
        return redirect('q2')
    form = RiskFactorForm()
    return render(request, 'riskfactorform.html', {'form': form})

def dyslexiaform(request):
    if request.method == 'POST':
        return redirect('q2')
    form = RiskFactorForm()
    return render(request, 'dyslexiaform.html', {'form': form})

def q2form(request):
    if request.method == 'POST':
        return redirect('q3')
    form = q2Form()
    return render(request, 'q2.html', {'form': form})

def q3form(request):
    if request.method == 'POST':
        return redirect('q4')
    form = q3Form()
    return render(request, 'q3.html', {'form': form})

def q4form(request):
    if request.method == 'POST':
        return redirect('q5')
    form = q4Form()
    return render(request, 'q4.html', {'form': form})

def q5form(request):
    if request.method == 'POST':
        return redirect('q6')
    form = q5Form()
    return render(request, 'q5.html', {'form': form})

def q6form(request):
    if request.method == 'POST':
        return redirect('q7')
    form = q6Form()
    return render(request, 'q6.html', {'form': form})

def q7form(request):
    if request.method == 'POST':
        return redirect('/')
    form = q7Form()
    return render(request, 'q7.html', {'form': form})