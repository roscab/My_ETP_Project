from django.db import models
from django import forms
from datetime import datetime

# Create your models here.
class Question(models.Model):
    SUBJECT_OPTIONS = [('ISTQB','ISTQB'),('OOP','Object Orientated Programming'),('Personal','Personal question'),('CAN','CAN'),('Logic','Logical question')]
    LEVEL_OPTIONS = [('Junior','Low'),('Profesional','Medium'),('Senior','High'),('N/A','Not applicable')]

    question = models.CharField(max_length=200)
    answer = models.TextField(null=True)
    subject = models.CharField(choices=SUBJECT_OPTIONS, max_length=200)
    dificulty_level = models.CharField(default='N/A', choices=LEVEL_OPTIONS, max_length=200)
    added_by = models.CharField(max_length=200)
    # created_at = models.DateTimeField(default=datetime.now, blank=True)
    
    def __str__(self):
        return self.question # this indicates the displayed value for each item under admin/questions ( text is a collumn of the table questions) 
    class Meta:
        verbose_name_plural = "Questions" # this changes the plural from admin page avooiding double 's'

class Candidate(models.Model):
    RECRUITER_OPTIONS = [('Guillermo','Guillermo Lopez'),('Vernonica','Verónica Mendes'),('Alberto','Alberto Arjona'),('Luisa','Luisa Cabrera'),('Oscar','Oscar Penon'),('Monika ','Monika Szymanska')]
    LEVEL_OPTIONS = [('Junior','Junior'),('Profesional','Profesional'),('Senior','Senior'),('Principle','Principle')]
    STATUS_OPTIONS = [('Pass recruiter interview','Pass recruiter interview'),('Rejected by recruiter','Rejected by recruiter'),('Pass technical interview','Pass technical interview'),('Rejected by technical interviewer','Rejected by technical interviewer'),('Pass BUL intreview','Pass BUL intreview'),('Rejected by BUL','Rejected by BUL'),('Pass client intreview','Pass client intreview'),('Rejected by client','Rejected by client'),('Rejected pre-offer','Rejected pre-offer'),('Rejected offer','Rejected offer')]
    GROUP_OPTIONS = [('Autosar','Autosar'),('Business analyst','Business analyst'),('C/C++','C/C++'),('DevOps','DevOps'),('Frontend','Frontend'),('iOS','iOS'),('Java','Java'),('.NET','.NET'),('Python','Python'),('QA','QA')]
    FORMAT_OPTIONS = [('new','new'),('old','old')]
    CONTACT_OPTIONS = [('Applied on his own','Applied on his own'),('LinkedIn','LinkedIn'),('Referred','Referred'),('Phone','Phone'),('No info','No info')] 
    TECHNICAL_VALIDATOR_OPTIONS = [('Bogdan Rosca','Bogdan Rosca'),('Eudes Costa','Eudes Costa'),('Daniel DeAmorim','Daniel DeAmorim')] 
    BUL_VALIDATOR_OPTIONS = [('Ana Diez','Ana Diez'),('Daniel DeAmorim','Daniel DeAmorim'),('Ramon Arque','Ramon Arque')] 
    BUL_VERDIC = [('Accepted','Accepted'),('Pending','Pendig'),('Rejected','Rejected')]

    name =  models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    skype = models.CharField(max_length=50,  blank=True)
    recruiter = models.CharField(choices=RECRUITER_OPTIONS, max_length=200)
    contact_date = models.DateField()
    contact_mode = models.CharField(choices=CONTACT_OPTIONS, max_length=200)
    technical_interview_date = models.DateField(default="2000-01-01")
    technical_interviewer = models.CharField(choices=TECHNICAL_VALIDATOR_OPTIONS, max_length=200)
    technical_feedback = models.CharField( max_length=9999, default="no info")
    technical_level = models.CharField(choices=LEVEL_OPTIONS,default='none', max_length=200, blank=True)
    bul_interview_date = models.DateField(default="2000-01-01")
    bul_interviewer = models.CharField(choices=BUL_VALIDATOR_OPTIONS, max_length=200, blank=True)
    bul_feedback = models.CharField( max_length=9999, default="no info")
    bul_verdic = models.CharField(choices=BUL_VERDIC, max_length=200, default="Pending")
    group = models.CharField(choices=GROUP_OPTIONS, max_length=200)
    status = models.CharField(choices=STATUS_OPTIONS, max_length=200, default="Pass recruiter interview")
    entry_format = models.CharField(choices=FORMAT_OPTIONS, max_length=200, default="new")
    
    def __str__(self):
        return self.name # this indicates the displayed value for each item under admin/questions ( text is a collumn of the table questions) 
    class Meta:
        verbose_name_plural = "Candidates" # this changes the plural from admin page avooiding double 's'