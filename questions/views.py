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

def recruiters(request):
    recruiter = "Veronica M."
    return render(request, 'candidates.html', {'recruiters': recruiters})

def questions(request):
    questions = Question.objects.all()
    return render(request, 'questions.html', {'questions': questions})

def data(request):
    data = {
        "total_no_candidates": Candidate.objects.count(),
        # domain
        "autosar_candidates": Candidate.objects.filter(group='Autosar').count(),
        "business_analyst_candidates": Candidate.objects.filter(group='Business analyst').count(),
        "c_candidates": Candidate.objects.filter(group='C/C++').count(),
        "devops_candidates": Candidate.objects.filter(group='DevOps').count(),
        "frontend_candidates": Candidate.objects.filter(group='Frontend').count(),
        "ios_candidates": Candidate.objects.filter(group='iOS').count(),
        "java_candidates": Candidate.objects.filter(group='Java').count(),
        "net_candidates": Candidate.objects.filter(group='.Net').count(),
        "python_candidates": Candidate.objects.filter(group='Python').count(),
        "qa_candidates": Candidate.objects.filter(group='QA').count(),
        "autosar_percentage":  round(Candidate.objects.filter(group='Autosar').count()/Candidate.objects.count()*100, 1),
        "business_analyst_percentage":  round(Candidate.objects.filter(group='Business analyst').count()/Candidate.objects.count()*100, 1),
        "c_percentage":  round(Candidate.objects.filter(group='C').count()/Candidate.objects.count()*100, 1),
        "devops_percentage":  round(Candidate.objects.filter(group='DevOps').count()/Candidate.objects.count()*100, 1),
        "frontend_percentage":  round(Candidate.objects.filter(group='Frontend').count()/Candidate.objects.count()*100, 1),
        "ios_percentage":  round(Candidate.objects.filter(group='iOS').count()/Candidate.objects.count()*100, 1),
        "java_percentage":  round(Candidate.objects.filter(group='Java').count()/Candidate.objects.count()*100, 1),
        "net_percentage": round(Candidate.objects.filter(group='.Net').count()/Candidate.objects.count()*100, 1),
        "python_percentage": round(Candidate.objects.filter(group='Python').count()/Candidate.objects.count()*100, 1),
        "qa_percentage": round(Candidate.objects.filter(group='QA').count()/Candidate.objects.count()*100, 1),
        # status
        "inProcess_candidates": Candidate.objects.filter(status='In process').count(),
        "standBy_candidates": Candidate.objects.filter(status='Stand by').count(),
        "passAllProcess_candidates": Candidate.objects.filter(status='Pass all process').count(),
        "rejectedTechnical_candidates": Candidate.objects.filter(status='Rejected technical interview').count(),
        "rejectedClientBULL_candidates": Candidate.objects.filter(status='Rejected by BUL/Client').count(),
        "rejectedRecruting_candidates": Candidate.objects.filter(status='Rejected by recruiter').count(),
        "rejectedPreOffer_candidates": Candidate.objects.filter(status='Rejected pre-offer').count(),
        "rejectedOffer_candidates": Candidate.objects.filter(status='Rejected offer').count(),
        "inProcess_percentage":  round(Candidate.objects.filter(status='In Process').count()/Candidate.objects.count()*100, 1),
        "standBy_percentage":  round(Candidate.objects.filter(status='Stand by').count()/Candidate.objects.count()*100, 1),
        "passAllProcess_percentage":  round(Candidate.objects.filter(status='Pass all process').count()/Candidate.objects.count()*100, 1),
        "rejectedTechnical_percentage":  round(Candidate.objects.filter(status='Rejected technical interview').count()/Candidate.objects.count()*100, 1),
        "rejectedClientBUL_percentage":  round(Candidate.objects.filter(status='Rejected by BUL/Client').count()/Candidate.objects.count()*100, 1),
        "rejectedRecruting_percentage":  round(Candidate.objects.filter(status='Rejected by recruiter').count()/Candidate.objects.count()*100, 1),
        "rejectedPreOffer_percentage":  round(Candidate.objects.filter(status='Rejected pre-offer').count()/Candidate.objects.count()*100, 1),
        "rejectedOffer_percentage": round(Candidate.objects.filter(status='Rejected offer').count()/Candidate.objects.count()*100, 1)
    }
    return render(request, 'data.html', {'data': data})