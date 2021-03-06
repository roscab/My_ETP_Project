from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

from .models import Question
from .models import Candidate

from .forms import NewCandidate
from .forms import NewStatus
from .forms import NewTechReport
from .forms import NewBulReport

# Create your views here.

def home(request):
    return render(request, 'home.html')

@login_required(login_url="/login")
def candidates(request):
    if request.method == 'POST':
        if 'submit_new_candidate' in request.POST:
            form = NewCandidate(request.POST)
            if form.is_valid():
                form.save()

        elif 'submit_new_status' in request.POST:
            entry_id = request.POST['entry_id']  # returns the entry id from database  
            instance = Candidate.objects.get(id=entry_id)
            status_form = NewStatus(request.POST or None, instance=instance)
            if status_form.is_valid():
                status_form.save()

    form = NewCandidate()
    status_form = NewStatus()
    candidates = Candidate.objects.all()
    
    return render(request, 'candidates.html', {'candidates': candidates,'form': form, 'status_form': status_form})

@login_required(login_url="/login")
def update_status(request):
    if request.method == 'POST':
        status_form = NewStatus(request.POST)
        if status_form.is_valid():
            status_form.save()

    status_form = NewStatus()
    candidates = Candidate.objects.all()
    return render(request, 'candidates.html', {'candidates': candidates,'status_form': status_form})    

@login_required(login_url="/login")
def questions(request):
    questions = Question.objects.all()
    return render(request, 'questions.html', {'questions': questions})

@login_required(login_url="/login")
def report(request):

    if request.method == 'POST':
        entry_id = request.POST['entry_id']  # returns the entry id from database  
        instance = Candidate.objects.get(id=entry_id)

        if (instance.status == 'Pass recruiter interview'):
            form_tech = NewTechReport(request.POST or None, instance=instance)
            if form_tech.is_valid():
                instance.status = 'Pass technical interview'
                form_tech.save() 
                
        elif 'submit_bul_feedback' in request.POST: 
            form_bul = NewBulReport(request.POST or None, instance=instance)
            if form_bul.is_valid():
                if form_bul.instance.bul_verdic == 'Accepted':
                    instance.status = 'Pass BUL interview'  
                else:
                    instance.status = 'Rejected by BUL'      
                form_bul.save()      
        
    form_tech = NewTechReport()
    form_bul = NewBulReport()
    candidates = Candidate.objects.all()
    return render(request, 'report.html', {'candidates': candidates,'form_tech': form_tech,'form_bul': form_bul })

@login_required(login_url="/login")
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
        "c_percentage":  round(Candidate.objects.filter(group='C/C++').count()/Candidate.objects.count()*100, 1),
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

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log in the user
            user = form.get_user()
            login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:    
                return redirect('home')
    else:
        form = AuthenticationForm()
        # form.fields['username'].widget.attrs['placeholder'] = "username"
        # form.fields['password'].widget.attrs['placeholder'] = "password"
    return render(request, "login.html",{'form':form})    

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
