from django.shortcuts import render
from django.http import HttpResponse

from .models import Question

# Create your views here.

def home(request):
    return render(request, 'home.html')

def questions(request):
    questions = Question.objects.all()
    return render(request, 'questions.html', {'questions': questions})

def table(request):
    questions = Question.objects.all()
    return render(request, 'table.html', {'questions': questions})