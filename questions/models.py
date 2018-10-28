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
    LEVEL_OPTIONS = [('Junior','Junior'),('Profesional','Profesional'),('Senior','Senior')]
    CLIENT_OPTIONS = [('ADP','ADP'),('FICOSA','FICOSA'),('HP','HP'),('Kaba','Kaba'),('Omrom','Omrom'),('Roche','Roche'),('Vueling','Vueling')]
    STATUS_OPTIONS = [('In process','In process'),('Stand By for other opportunities','Stand By for other opportunities'),('Pass all process','Pass all process'),('Rejeced after techncal interview','Rejeced after techncal interview'),('Rejeced by BUL','Rejeced by BUL'),('Rejeced by client','Rejeced by client'),('Descarded REC','Descarded REC'),('Reject pre-offer','Reject pre-offer'),('Reject Offer','Reject Offer')]
    GROUP_OPTIONS = [('C/C++','C/C++'),('Backend','Backend'),('Frontend','Frontend'),('Phyton','Phyton'),('QA','QA'),('.NET','.NET')]

    name = models.CharField(max_length=200)
    recruiter = models.CharField(choices=RECRUITER_OPTIONS, max_length=200)
    contac_date = models.DateField()
    technical_interview_date = models.DateField()
    level = models.CharField(choices=LEVEL_OPTIONS, max_length=200)
    bul_interview_date = models.DateField()
    client = models.CharField(choices=CLIENT_OPTIONS, max_length=200)
    group = models.CharField(choices=GROUP_OPTIONS, max_length=200)
    status = models.CharField(choices=STATUS_OPTIONS, max_length=200)
    next_step = models.CharField(max_length=200)
    # created_at = models.DateTimeField(default=datetime.now, blank=True)
    
    def __str__(self):
        return self.name # this indicates the displayed value for each item under admin/questions ( text is a collumn of the table questions) 
    class Meta:
        verbose_name_plural = "Candidates" # this changes the plural from admin page avooiding double 's'