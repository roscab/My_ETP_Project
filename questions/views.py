from django.shortcuts import render
from django.http import HttpResponse

from .models import Question
from .models import Candidate

# Create your views here.

def home(request):
    return render(request, 'home.html')

def candidates(request):
    candidates = Candidate.objects.all()
    return render(request, 'candidates.html', {'candidates': candidates})

def questions(request):
    questions = Question.objects.all()
    return render(request, 'questions.html', {'questions': questions})
