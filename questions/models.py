from django.db import models
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
    RECRUITER_OPTIONS = [('Guillermo','Guillermo Lopez'),('Vernonica','Verónica Mendes'),('Alberto','Alberto Arjona'),('Luisa','Luisa Cabrera'),('Oscar','Oscar Penon'),('Monika','Monika Szymanska')]
    LEVEL_OPTIONS = [('Junior','Junior'),('Junior-Low','Junior-Low'),('Junior-High','Junior-High'),('Profesional','Profesional'),('Profesional-Low','Profesional-Low'),('Profesional-High','Profesional-High'),('Senior','Senior'),('Senior-Low','Senior-Low'),('Senior-High','Senior-High')]
    STATUS_OPTIONS = [('In process','In process'),('Stand by','Stand by'),('Pass all process','Pass all process'),('Rejected technical interview','Rejected technical interview'),('Rejected by BUL','Rejected by BUL'),('Rejected by client','Rejected by client'),('Rejected by recruiter','Rejected by recruiter'),('Rejected pre-offer','Rejected pre-offer'),('Rejected offer','Rejected offer')]
    GROUP_OPTIONS = [('Autosar','Autosar'),('Business analyst','Business analyst'),('C/C++','C/C++'),('DevOps','DevOps'),('Frontend','Frontend'),('iOS','iOS'),('Java','Java'),('.NET','.NET'),('Python','Python'),('QA','QA')]

    name = models.CharField(max_length=200)
    recruiter = models.CharField(choices=RECRUITER_OPTIONS, max_length=200)
    contact_date = models.DateField()
    technical_interview_date = models.DateField()
    technical_interviewer = models.CharField(max_length=200)
    technical_level = models.CharField(choices=LEVEL_OPTIONS,default='none', max_length=200)
    bul_interview_date = models.DateField()
    bul_intervier = models.CharField(max_length=200)
    group = models.CharField(choices=GROUP_OPTIONS, max_length=200)
    status = models.CharField(choices=STATUS_OPTIONS, max_length=200)
    # next_step = models.CharField(max_length=200)
    # created_at = models.DateTimeField(default=datetime.now, blank=True)
    
    def __str__(self):
        return self.name # this indicates the displayed value for each item under admin/questions ( text is a collumn of the table questions) 
    class Meta:
        verbose_name_plural = "Candidates" # this changes the plural from admin page avooiding double 's'