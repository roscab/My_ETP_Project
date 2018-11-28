from django.db import models
from django import forms
from datetime import datetime

# Create your models here.
class Question(models.Model):
    SUBJECT_OPTIONS = [('Autosar','Autosar'),('CAN','CAN'),('C/C++','C/C++'),('ISTQB','ISTQB'),('Java','Java'),('Logic','Logical question'),
                         ('.NET','.NET'),('OOP','Object Orientated Programming'),('Personal','Personal question'),('Python','Python')]
    LEVEL_OPTIONS = [('Junior','Low'),('Professional','Medium'),('Senior','High'),('N/A','Not applicable')]
    STATUS_OPTIONS = [('Review pending','Review pending'),('Reviewed','Reviewed')]

    question = models.CharField(max_length=200)
    answer = models.TextField(null=True)
    subject = models.CharField(choices=SUBJECT_OPTIONS, max_length=200)
    dificulty_level = models.CharField(default='N/A', choices=LEVEL_OPTIONS, max_length=200)
    added_by = models.CharField(max_length=200)
    status = models.CharField(default='Review panding', choices=STATUS_OPTIONS, max_length=200)
    # created_at = models.DateTimeField(default=datetime.now, blank=True)
    
    def __str__(self):
        return self.question # this indicates the displayed value for each item under admin/questions ( text is a collumn of the table questions) 
    class Meta:
        verbose_name_plural = "Questions" # this changes the plural from admin page avooiding double 's'

class Candidate(models.Model):
    RECRUITER_OPTIONS = [('Alberto','Alberto Arjona'),('Claudia','Claudia Perarnau'),('Guillermo','Guillermo Lopez'),('Luisa','Luisa Cabrera'),
                         ('Monika ','Monika Szymanska'),('Oscar','Oscar Penon'),('Verónica','Verónica Mendes')]
    LEVEL_OPTIONS = [('Junior','Junior'),('Professional','Professional'),('Senior','Senior'),('Principle','Principle')]
    STATUS_OPTIONS = [('Pass recruiter interview','Pass recruiter interview'),('Rejected by recruiter','Rejected by recruiter'),
                      ('Pass technical interview','Pass technical interview'),('Rejected by technical interviewer','Rejected by technical interviewer'),
                      ('Pass BUL interview','Pass BUL interview '),('Rejected by BUL','Rejected by BUL'),('Pass client intreview','Pass client intreview'),
                      ('Rejected by client','Rejected by client'),('Rejected pre-offer','Rejected pre-offer'),('Rejected offer','Rejected offer')]
    GROUP_OPTIONS = [('Autosar','Autosar'),('Business analyst','Business analyst'),('C/C++','C/C++'),('DevOps','DevOps'),('Frontend','Frontend'),('iOS','iOS'),('Java','Java'),
                     ('.NET','.NET'),('Python','Python'),('QA','QA')]
    FORMAT_OPTIONS = [('new','new'),('old','old')]
    CONTACT_OPTIONS = [('Join ERNI','Join ERNI'),('Head hunter','Head hunter'),('Infojobs','Infojobs'),('Internal referral','Internal referral'),
                       ('LinknedIn application','LinknedIn application'),('LinknedIn search','LinknedIn search'),('Other jobs portals','Other jobs portals'),('Universities','Universities')] 
    TECHNICAL_VALIDATOR_OPTIONS = [('Bogdan Rosca','Bogdan Rosca'),('Daniel De Amorim','Daniel De Amorim'),('Eudes Costa','Eudes Costa'),('Eduardo Benito','Eduardo Benito'),
                                   ('Hernan Bartoletti','Hernan Bartoletti'),('Javier Cabo','Javier Cabo'),('Paul Melero','Paul Melero'),('Ruben Manzano','Ruben Manzano'),
                                   ('Victor Carrascal','Victor Carrascal'),('Vinicius Scheidegger','Vinicius Scheidegger')] 
    BUL_VALIDATOR_OPTIONS = [('Alfons Martinez','Alfons Martinez'),('Albert Alsina','Albert Alsina'),('Arnau Roca','Arnau Roca'),('Ana Diez','Ana Diez'),
                            ('Christian Fuentes','Christian Fuentes'),('Daniel DeAmorim','Daniel DeAmorim'),('Juan Bernardo','Juan Bernardo'),('Lara Hernandez','Lara Hernandez'),
                            ('Marc Baguena','Marc Baguena'),('Ramon Arque','Ramon Arque'),('Samuel Chicon','Samuel Chicon'),('Victor Carrascal','Victor Carrascal')] 
    BUL_VERDIC = [('Accepted','Accepted'),('Rejected','Rejected')]

    name =  models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    skype = models.CharField(max_length=50,  blank=True)
    recruiter = models.CharField(choices=RECRUITER_OPTIONS, max_length=200)
    contact_date = models.DateField()
    contact_mode = models.CharField(choices=CONTACT_OPTIONS, max_length=200)
    technical_interview_date = models.DateField(default="2000-01-01")
    technical_interviewer = models.CharField(choices=TECHNICAL_VALIDATOR_OPTIONS, max_length=200)
    technical_feedback = models.CharField( max_length=9999, default="Pending")
    technical_level = models.CharField(choices=LEVEL_OPTIONS,default='', max_length=200, blank=True)
    bul_interview_date = models.DateField(default="2000-01-01")
    bul_interviewer = models.CharField(choices=BUL_VALIDATOR_OPTIONS, max_length=200, blank=True)
    bul_feedback = models.CharField( max_length=9999, default="Pending")
    bul_verdic = models.CharField(choices=BUL_VERDIC, max_length=200, default="Pending")
    group = models.CharField(choices=GROUP_OPTIONS, max_length=200)
    status = models.CharField(choices=STATUS_OPTIONS, max_length=200, default="Pass recruiter interview")
    entry_format = models.CharField(choices=FORMAT_OPTIONS, max_length=200, default="new")
    
    def __str__(self):
        return self.name # this indicates the displayed value for each item under admin/questions ( text is a collumn of the table questions) 
    class Meta:
        verbose_name_plural = "Candidates" # this changes the plural from admin page avooiding double 's'